from socket import *
import re
import thread
import sys
import time
import numpy as np
import cv2
import pickle
def dist(x,y):
    return np.sqrt(np.sum((x-y)**2))

def serve(connection,addr,naming,recognizer):
	while True: 
		data=""
		while True:           
		   	a=connection.recv(4096)   
		   	data=data+a
		   	if len(data) == 57600:
		   		break                                        
		face = np.fromstring(data, dtype=np.uint8)
		print len(face)
		face=face[0:57600]
		if len(face) != 57600:
			connection.sendall("corrupt_data")
			continue
		face=np.reshape(face,(240,240))
		prediction = recognizer.predict(face)
		connection.sendall(str(naming[prediction]))
		#connection.sendall('\n')
	connection.close()
	sys.exit()
database=np.load("data.npy")
locations=np.load("locations.npy")
labels=np.load("labels.npy")

naming=np.load("naming.npy")
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load("database.yml")
if len(sys.argv) != 2:
	print 'USAGE python server.py <port>'
	exit(0)
port=int(sys.argv[1])

mysock = socket(AF_INET,SOCK_STREAM)                                                   #start listening on localhost
#mysock.bind(('127.0.0.1',port))  
mysock.bind(('10.42.0.1',port))   
print 'server running at 127.0.0.1:',port                                       
mysock.listen(1000)                                                                
while True:
	conn,addr = mysock.accept()
	print 'connected with '+addr[0]+':'+str(addr[1])
	#conn.sendall('we support following requests\nGET api/serverStatus\nGET api/request?connId=<connection_id>&timeout=<time>\nPUT api/kill?connId=<connection_id>\n\n')
	thread.start_new_thread(serve,(conn,addr,naming,recognizer))
	
