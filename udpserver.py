import socket
import sys
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' %server_address
sock.bind(server_address)
while True:
	print >>sys.stderr, '\nwaiting to receive input'
	input, address = sock.recvfrom(4096)
	lists = input.split(',')
	first = lists[0]
	second  = lists[1]
	first_value = first.split(' ')[1]
	second_value = second.split(' ')[1]
	if first_value == '"valid"':
		fp = open("valid.log", "a")
		sent = second_value + '\n'
		fp.write(sent)
		fp.close()
		#print second_value
	else:
		#print "invalid" + second_value
		fp = open("invalid.log", "a")
		sent = second_value + "\n"
		fp.write(sent)
		fp.close()
	#print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
	#print >>sys.stderr, data
	#if data:
	#	sent = sock.sendto(data, address)
    #	print >>sys.stderr, 'sent %s bytes back to %s' % (sent, address)'''
    
    

