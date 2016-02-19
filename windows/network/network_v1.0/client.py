#!/usr/bin/python

import socket

s = socket.socket()
host = "10.46.158.106"
port = 12345

s.connect((host, port))
print s.recv(1024)

#command = 'start'
#s.send(command)

print s.recv(1024)
#print s.recv(1024)

s.close
