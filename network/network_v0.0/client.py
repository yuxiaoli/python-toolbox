#!/usr/bin/python

import socket

s = socket.socket()
host = "10.46.162.252"
port = 12345

s.connect((host, port))
print s.recv(1024)

#'..\\bat\\start_lync.bat'
#'..\\bat\\kill_lync.bat'
command = '..\\bat\\kill_lync.bat'
print command
s.send(command)

print s.recv(1024)
#print s.recv(1024)

s.close
