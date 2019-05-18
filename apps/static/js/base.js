/*
*@author:Imtinmin
*@date: 19-5-16
*@github:https://github.com/imtinmin
* */
function getXmlhttp(){
	var xmlhttp;
    if (window.XMLHttpRequest)
    {
        //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp=new XMLHttpRequest();
    }
    else
    {
        // IE6, IE5 浏览器执行代码
        xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    return xmlhttp;
}

function getID(id) {
    return document.getElementById(id);
}

function getName(name) {
    return document.getElementsByName(name);
}