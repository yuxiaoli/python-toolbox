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
	

def deploy(filename):
	# Update pip
	#cmd = "python -m pip install --upgrade pip"
	#os.system(cmd)

	path, name = os.path.split(filename)
	#print(path)
	#print(name)
	

	f = open(filename, 'r', encoding="utf8")
	txt = f.read()
	#print(txt)
	
	pattern = "^pip install (?P<lib>[\S ]+)\n"
	libs = re.findall(pattern, txt, re.MULTILINE)
	#print(libs)
	
	libs = set(libs)
	#print(libs)
	for lib in libs:
		cmd = "pip install " + lib + " --target " + path + " --upgrade --quiet"
		print(cmd)
		os.system(cmd);
		
	#package(path)
	return
	
if __name__ == "__main__":
	fname = sys.argv[1]
	deploy(fname)