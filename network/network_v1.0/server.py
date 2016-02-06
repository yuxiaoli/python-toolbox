#!/usr/bin/python

import socket
import os
import shutil
import sys


def main():

	# default root is C:\gateway
	root = "C:\gateway"
	
	# option to get current dir
	# root = os.getcwd()

	s = socket.socket()
	host = socket.gethostname()
	port = 12345
	s.bind((host, port))

	s.listen(5)
	while True:
		c, addr = s.accept()
		print 'Got connection from', addr
		c.send('connected')

		# to do - kick off a new thread

		client = str(addr[0]) + "-" + str(addr[1])
		# print client
		os.chdir(root)
		os.system("mkdir " + client)
		client_path = root + "\\" + client
		cwd_buf = client_path + "\\cwd.txt"
		out_buf = client_path + "\\out.txt"
		# cmd_bat = cwd + "\\" + client + "\\cmd.bat"

		with open(cwd_buf, 'w') as f:
			f.write(root)

		while True:
			
		
			with open(cwd_buf, 'r') as f:
				cwd = f.read()
			# cwd = cwd[:-2]
			print cwd

			os.chdir(cwd)
			c.send(cwd)
			
			cmd = c.recv(1024)
			print cmd
			if cmd == "quit":
				break
			else:
				with open("cmd.bat", 'w') as f:
					f.write(cmd + " 1> " + "\"" + out_buf + "\"" + " 2>&1\n")
					f.write("pwd 1> " + "\"" + cwd_buf + "\"" + " 2>&1\n")
					# f.write("echo %cd% 1> " + "\"" + cwd_buf + "\"" + " 2>&1\n")

				# p = subprocess.Popen('start cmd.bat', shell=True, stdout=subprocess.PIPE)
				# p.wait()
				os.system("cmd.bat")
				# to do - client hangs for any blocking call, need other process come in to kill this process and clean up
				
				# delete cmd.bat
				os.remove("cmd.bat")
				print "cmd.bat deleted"

				# modify cwd
				# read
				with open(cwd_buf, 'r') as f:
					# read
					path = f.read()
					drive = path[10].upper()
					path = drive + ":" + path[11:-1].replace('/', '\\')
					print path
				# then write
				with open(cwd_buf, 'w') as f:
					f.write(path)

				# out = str(os.system(cmd))
				with open(out_buf, 'r') as f:
					out = f.read()
				print out
				if not out:
					out = "none"


				c.send(out)
			
		c.send('closing client on server')
		# delete client folder
		shutil.rmtree(client_path)
		c.close()



if __name__ == "__main__":
	main()
	