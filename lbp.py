import numpy as np
import os
import cv2
import sys
def calclbp(a):                                                                       #dimension of a is 3x3
	h,w=a.shape
	if h != 3 or w !=3:
		print "wrong size of filter",h,w
		return 1
	first=a[0][0]>a[1][1]                                                         #checking all 8 bits
	second=a[0][1]>a[1][1]
	third=a[0][2]>a[1][1]
	fourth=a[1][2]>a[1][1]
	fifth=a[2][2]>a[1][1]
	sixth=a[2][1]>a[1][1]
	seventh=a[2][0]>a[1][1]
	eigth=a[1][0]>a[1][1]
	a=np.array([first,second,third,fourth,fifth,sixth,seventh,eigth],dtype=int)
	sum=0                                                                         #converting 8 digit binary to decimal
	j=128
	for i in a:
		sum=sum+i*j
		j=j/2
	return sum                                                                    #return lbp of one pixel
def lbp(a):
	height,width=a.shape
	b=a
	a=np.pad(a,((1,1),(1,1)),mode='constant')
	print a
	i=1
	while i <= width:
		j=1
		while j <= height:
			filt=a[i-1:i+2,j-1:j+2]
			print filt
			b[i-1][j-1]=calclbp(filt)                                     #pass 3x3 filter to lbp calculator
			j+=1
		i+=1
	return b
a=cv2.imread("Lenna.png",0)
#a=cv2.resize(a,(64,64))
b=lbp(a)
cv2.imshow("lbp",b)
cv2.waitKey(0)
			
	

