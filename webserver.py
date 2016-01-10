import socket
import string
import random
import time

HOST, PORT = '', 8888
def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))
	#return "abc123"

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(5)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    #http_response = """\
#HTTP/1.1 200 OK

#Hello, World!
#"""
    #client_connection.sendall(http_response)
    #request = client_connection.recv(1024)
    #print request
    ids={}
    #start_time=int(time.time())

    request = client_connection.recv(1024)
    #print request
    if request=='/generate':
    	now_key=id_generator()
    	ids[now_key] = int(time.time())
    	client_connection.sendall(str(now_key))
    elif request == '/validate':
    	#now_time=int(time.time())
    	#sec=now_time-start_time
    	for key,item in ids.iteritems():
    		if time.time()-item >59:
    			ids[key]=0
    	key = raw_input()
    	if(ids[key]<>0):
    		client_connection.sendall('valid')
    	else:
    		client_connection.sendall('invalid')
    elif request == '/delete':
    	key=raw_input()
    	ids[key]=0
    request = client_connection.recv(1024)
    #print request
    if request=='/generate':
    	now_key=id_generator()
    	ids[now_key] = int(time.time())
    	client_connection.sendall(str(now_key))
    elif request == '/validate':
    	#now_time=int(time.time())
    	#sec=now_time-start_time
    	for key,item in ids.iteritems():
    		if time.time()-item >59:
    			ids[key]=0
    	key = raw_input()
    	if(ids[key]<>0):
    		client_connection.sendall('valid')
    	else:
    		client_connection.sendall('invalid')
    elif request == '/delete':
    	key=raw_input()
    	ids[key]=0
    client_connection.close()
    break
