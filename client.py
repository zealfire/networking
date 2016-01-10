import socket
import time
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server='localhost'
port=8888
#print "hell"
#print int(time.time())
s.connect((server,port))
#print s.recv(1024)
#s.send("alok")
string = raw_input()
#print string
s.send(string)
print s.recv(1024)
string1=raw_input()
s.send(string1)
print s.recv(1024)
s.close()
