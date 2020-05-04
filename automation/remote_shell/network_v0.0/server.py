#!/usr/bin/python

import socket
import os
import subprocess

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
	c, addr = s.accept()
	print 'Got connection from', addr
	c.send('connected')
	command = c.recv(1024)
	print command
	#command = r'\\harv-c-ghenry\public\toolbox\reboot.bat'
	#command = 'start'
	subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	
	c.send('done')
	c.close()
