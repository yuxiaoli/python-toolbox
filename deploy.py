import sys
import re
import os
import shutil

def package(dirname):
	path, name = os.path.split(dirname)
	#print(path)
	#print(name)
	
	# Zip folder
	shutil.make_archive(name, 'zip', dirname)
	

def deploy(filename, options=["--upgrade", "--quiet"]):
	opt = ""
	for option in options:
		opt += " " + option

	path, name = os.path.split(filename)
	#print(path)
	#print(name)
	

	f = open(filename, 'r', encoding="utf8")
	txt = f.read()
	#print(txt)
	
	pattern = "^pip install (?P<modules>[\S ]+)\n"
	result = re.findall(pattern, txt, re.MULTILINE)
	#print(result)
	
	libs = set()
	for modules in result:
		modules = modules.split()
		for module in modules:
			libs.add(module)
	
	#print(libs)
	for lib in libs:
		#cmd = "pip install " + lib + " --target " + path + " --upgrade --quiet"
		cmd = "pip install " + lib + opt
		print(cmd)
		os.system(cmd);
		
	#package(path)
	return
	
def install_pip():
	cmd = "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"
	os.system(cmd)
	cmd = "python get-pip.py"
	os.system(cmd)
	
if __name__ == "__main__":
	install_pip()
	fname = sys.argv[1]
	deploy(fname)