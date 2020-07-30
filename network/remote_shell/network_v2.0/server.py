#!/usr/bin/env python

"""
An echo server that uses threads to handle multiple clients at a time.
Entering any line of input at the terminal will exit the server.
"""
# to do
# 1. each client thread on the server needs to have a signature (use pid)
# 2. cleanup for forced close - server side & client side

import select
import socket
import sys
import threading

import os
import shutil

class Server:
	def __init__(self):
		self.host = ''
		self.port = 50000
		self.backlog = 5
		self.size = 1024
		self.server = None
		self.threads = []

	def open_socket(self):
		try:
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server.bind((self.host,self.port))
			self.server.listen(5)
		except (socket.error, (value,message)):
			if self.server:
				self.server.close()
			print("Could not open socket: " + message)
			sys.exit(1)

	def run(self):
		self.open_socket()
		
		running = 1
		while running:
			try:
				c = Client(self.server.accept())
				print('Got connection from', c.address)
				c.start()
				self.threads.append(c)
			except KeyboardInterrupt:
				running = 0
		

		# close all threads

		self.server.close()
		for c in self.threads:
			c.join()

class Client(threading.Thread):
	def __init__(self, client_address):
		threading.Thread.__init__(self)
		self.client = client_address[0]
		self.address = client_address[1]
		self.size = 1024
		# default root is C:\gateway
		self.root = "C:\gateway"
		# option to get current dir
		# self.root = os.getcwd()

	def run(self):
		
		running = 1
		# while running:
			# data = self.client.recv(self.size)
			# if data:
				# self.client.send(data)
			# else:
				# self.client.close()
				# running = 0
				
		c = self.client
		c.sendall('connected'.encode('ascii'))

		client = str(self.address[0]) + "-" + str(self.address[1])
		# print client
		os.chdir(self.root)
		os.system("mkdir " + client)
		client_path = self.root + "\\" + client
		cwd_buf = client_path + "\\cwd.txt"
		out_buf = client_path + "\\out.txt"
		# cmd_bat = cwd + "\\" + client + "\\cmd.bat"

		with open(cwd_buf, 'w') as f:
			f.write(self.root)
		
		while running:
		
			with open(cwd_buf, 'r') as f:
				cwd = f.read()
			# cwd = cwd[:-2]
			print(cwd)

			os.chdir(cwd)
			c.send(cwd.encode('ascii'))
			
			cmd = c.recv(self.size).decode('ascii')
			print(cmd)
			if cmd == "quit":
				running = 0
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
				# to do - if cmd.bat was not deleted by the cmd itself
				os.remove("cmd.bat")
				print("cmd.bat deleted")

				# modify cwd
				# read
				with open(cwd_buf, 'r') as f:
					# read
					path = f.read()
					drive = path[10].upper()
					path = drive + ":" + path[11:-1].replace('/', '\\')
					print(path)
				# then write
				with open(cwd_buf, 'w') as f:
					f.write(path)

				# out = str(os.system(cmd))
				with open(out_buf, 'r') as f:
					out = f.read()
				print(out)
				if not out:
					out = "none"


				c.send(out.encode('ascii'))
			
		c.send('closing client on server'.encode('ascii'))
		# delete client folder
		shutil.rmtree(client_path)
		c.close()

if __name__ == "__main__":
	s = Server()
	s.run()

