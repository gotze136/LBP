import os
import sys
import numpy as np
import cv2
path=sys.argv[1]
naming=[]
labels=[]
locations=[]
data=[]
recognizer = cv2.face.createLBPHFaceRecognizer()
k=0
for folders in os.listdir(path):
	folder=path+'/'+folders
	naming.append(folders)
	for images in os.listdir(folder):
		image=folder+'/'+images
		print image
		locations.append(image)
		labels.append(k)
		i=cv2.imread(image,0)
		i=cv2.resize(i,(240,240))
		#i=calcgrad(i)
		#j=hist(i)
		data.append(i)
	k=k+1
print "training"
recognizer.train(np.array(data), np.array(labels))
recognizer.save("database.yml")
np.save("naming",np.array(naming))
np.save("labels",np.array(labels))
np.save("locations",np.array(locations))
np.save("data",np.array(data))
