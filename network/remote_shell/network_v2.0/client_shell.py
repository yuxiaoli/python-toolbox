#!/usr/bin/python

import socket


def main():
	host = "localhost"
	port = 50000
	size = 1024
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	print(s.recv(1024).decode('ascii'))

	while True:
		cwd = s.recv(1024).decode('ascii')
		cmd = input("[" + host + "]" + cwd + ">")
		s.send(cmd.encode('ascii'))
		if cmd == "quit":
			break
		else:
			out = s.recv(1024).decode('ascii')
			if (out != "none"):
				print(out)


	print(s.recv(1024).decode('ascii'))
	#print s.recv(1024)

	s.close



if __name__ == "__main__":
	main()
	