import numpy as np
import os
import sys
import cv2
def calclbp(a):
	h,w=a.shape
	if h != 3 or w !=3:
		print "wrong size of filter",h,w
		return 1
	first=a[0][0]>a[1][1]
	second=a[0][1]>a[1][1]
	third=a[0][2]>a[1][1]
	fourth=a[1][2]>a[1][1]
	fifth=a[2][2]>a[1][1]
	sixth=a[2][1]>a[1][1]
	seventh=a[2][0]>a[1][1]
	eigth=a[1][0]>a[1][1]
	#print first,second,third,fourth,fifth,sixth,seventh,eigth
	a=np.array([first,second,third,fourth,fifth,sixth,seventh,eigth],dtype=int)
	#print a
	sum=0
	j=128
	for i in a:
		sum=sum+i*j
		j=j/2
	#print sum
	return sum
def lbp(a):
	height,width=a.shape
	b=a
	a=np.pad(a,((1,1),(1,1)),mode='constant')
	#print a
	i=1
	while i <= width:
		j=1
		while j <= height:
			filt=a[i-1:i+2,j-1:j+2]
			#print filt
			b[i-1][j-1]=calclbp(filt)
			j+=1
		i+=1
	return b
naming=np.load("naming.npy")
data=np.load("data.npy")
locations=np.load("locations.npy")
labels=np.load("labels.npy")
recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load("database.yml")
'''print naming
print data
print locations
print labels

'''
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

camera=cv2.VideoCapture(0)
while True:
	ret,frame=camera.read()
	gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray,1.8,5)
	for (x,y,w,h) in faces:
		face=gray[y: y + h, x: x + w]
		face=np.array(face,'uint8')
		#cv2.imshow("face",face)
		#nbr_predicted, conf = recognizer.predict(face)
		#print nbr_predicted
	
		gray=cv2.resize(gray,(240,240))
		predict=recognizer.predict(gray)
		print naming[predict]
	
	#cv2.imshow("lbp",model)
		
	cv2.imshow("original",frame)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
camera.release()
cv2.destroyAllWindows()
