/*
*@author:Imtinmin
*@date: 19-5-16
*@github:https://github.com/imtinmin
* */

var getfileurl = "/api/fileList?url=http://39.108.36.103:9999/upload/tinmin.php&pwd=tinmin"; 

function getfileList(url,pwd){
var getfileurl = "/api/fileList?url="+url+"&pwd="+pwd;
var xmlhttp = getXmlhttp();
xmlhttp.onreadystatechange=function()
  {
  if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
    var s = eval(xmlhttp.responseText);
    for (var i = 0; i < s.length; i++) {
    	document.write(s[i]['filename']+s[i]['permiss']+s[i]['time']+s[i]['size']);
    }
    }
  }
xmlhttp.open("GET",getfileurl,true);
xmlhttp.send();
}


function getform(){
	var url = getName('url').innerHTML;
	var pwd = getName('pwd').innerHTML;
	getfileList(url,pwd)
}