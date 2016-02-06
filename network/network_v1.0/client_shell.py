#!/usr/bin/python

import socket


def main():
	s = socket.socket()
	host = "10.46.162.222"
	port = 12345

	s.connect((host, port))
	print s.recv(1024)

	while True:
		cwd = s.recv(1024)
		cmd = raw_input("[" + host + "]" + cwd + ">")
		s.send(cmd)
		if cmd == "quit":
			break
		else:
			out = s.recv(1024)
			if (out != "none"):
				print out


	print s.recv(1024)
	#print s.recv(1024)

	s.close



if __name__ == "__main__":
	main()
	