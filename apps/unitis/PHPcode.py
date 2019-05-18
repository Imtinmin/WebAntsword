import base64
#获取当前路径
def test():
	code  = "echo 1;"
	return code
def getfiledir():
	code = "echo dirname(__file__);"
	return code

#获取当前目录
def getfilelist():
	code = "var_dump(scandir('./'));"
	return code

def getFilePathBase(path):
	code = """
	$handle = opendir('"""+path+"""');
	$file = array();
	$res = array();
	$i = 0;
	while (($file = readdir($handle)) !== false) {
		$f['filename'] = $file;
		$f['permiss'] = substr(sprintf('%o', fileperms($file)), -4);
		$f['time'] = date('Y-m-d H:i:s',filemtime($file));
		$f['size'] = filesize($file);
		$res[$i] = $f;$i++;
	}
	echo ('<ek>');echo json_encode($res);echo ('<ek>');
	"""
	return code

def scandir(path):
	code = "var_dump(scandir('"+path+"'));"
	return code

def catfile(filename):
	code = "readfile('"+filename+"');"
	return code