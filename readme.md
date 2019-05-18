# WEB蚁剑计划

参考：https://github.com/iceyhexman/WCnife

## 脚本语言
python3 flask

## 功能
连接webshell(eval马)
写入文件，删除文件，能查看目录结构，显示权限，能切换目录
显示之前连接的数据(emmm sqlite3实现吧,不知道能不能实现)

每日进展
5.17
增加重命名和修改数据弹出框，对无session访问/board报错进行处理，重定向到根目录，



5.25 之前完成目录翻阅

出现问题：
1.提交url和pwd是用表单提交直接跳转到board控制台还是ajax请求返回json再进行跳转操作
2.目录翻阅如何ajax请求更新目录列表，将查看的目录放置于session取出还是其他方法