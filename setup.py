import os
from deploy import *

def install(filename='.'):
	for root, dirs, files in os.walk(filename):
		for file in files:
			if (file.endswith('.py')):
				fname = os.path.join(root, file)
				#print(fname)
				
				# Deploy file
				deploy(fname)
		

if __name__ == "__main__":
	install_pip()
	install()
	
