#!/usr/bin/python
# -*- coding: utf-8 -*-

document='''

//===============================
//hiking_mixing_image.py
//===============================
... mix images random position

arguments
    1.targetdirectory
        ex) ./
    (2.backgroundimage):default => white
    (3.widthsize):default => 512[px]
    (4.heightsize):default => 512[px]
    (5.outputpath):default => ./temp.jpg

'''

from opencv.cv import *
from opencv.highgui import *
#import hiking_tegaki_pypackage.modules as tegaki
#import hiking_tegaki_pypackage.cv as tegakicv
import math
import sys
import os
import random

#==============
#main function
#==============
if(__name__=='__main__'):
    print "\n######################"

    #-----------------------
    #I/O
    #-----------------------
    if(len(sys.argv)<=1):
        print document
        exit(0)
 
    targetpath=sys.argv[1]
    #default
    bgpath=0
    widthsize=512
    heightsize=512
    outputpath="temp.jpg"
    
    if(len(sys.argv)>=3):
        bgpath=sys.argv[2]
        print "background image:",bgpath
    if(len(sys.argv)>=4):
        widthsize = int(sys.argv[3])
        heightsize = int(sys.argv[3])
    if(len(sys.argv)>=5):
        heightsize = int(sys.argv[4])
    if(len(sys.argv)>=6):
        outputpath = sys.argv[5]

    print "targetdirectory:",targetpath
    print "output:",outputpath
    print "widthsize:",widthsize
    print "heightsize:",heightsize

    #--------------------
    #read
    #--------------------
    filelist = os.listdir(targetpath)
    print "list",filelist

    imagelist=[]
    for file in filelist:
        if(file.find("jpg")>0):
            imagelist.append(cvLoadImage(targetpath+"/"+file))
        elif(file.find("JPG")>0):
            imagelist.append(cvLoadImage(targetpath+"/"+file))
        elif(file.find("png")>0):
            imagelist.append(cvLoadImage(targetpath+"/"+file))
    #print "imagelist",imagelist

    if(bgpath):
        image_target = cvLoadImage(bgpath)
        image_resize = cvCreateImage(cvSize(widthsize, heightsize), IPL_DEPTH_8U, 3)
        cvResize(image_target, image_resize, CV_INTER_NN)
    else:
        image_target = cvCreateImage(cvSize(widthsize, heightsize), IPL_DEPTH_8U, 3)
        cvZero(image_target)
        cvNot(image_target, image_target)

    #---------------------------
    #paste to target background
    #---------------------------
    roi=cvRect(0, 0, 0, 0)
    for image in imagelist:
        
        #size:
        if(image.width>=image.height):
            roi.width = random.randint(10,widthsize/2)
            roi.height = roi.width * image.height/image.width
        else:
            roi.height = random.randint(10, heightsize/2)
            roi.width = roi.height * image.width/image.height

        image_resize = cvCreateImage(cvSize(roi.width, roi.height), IPL_DEPTH_8U, 3)        
        cvResize(image, image_resize, CV_INTER_NN) #resize image -> image_resize

        #position:
        roi.x=random.randint(0, widthsize-roi.width)
        roi.y=random.randint(0, heightsize-roi.height)

        sub = cvGetSubRect(image_target, roi)
        cvCopy(image_resize, sub)

    cvSaveImage( outputpath, image_target)
    exit(0)
