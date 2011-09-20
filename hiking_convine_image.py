#!/usr/bin/python
# -*- coding: utf-8 -*-

document='''

//===============================
//hiking_convine_image.py
//===============================
...convine image in directory

arguments
    1.targetdirectory
    (2.outputfile):default=>temp.jpg
    (3.widthsize):default=>1

'''

from opencv.cv import *
from opencv.highgui import *
#import hiking_tegaki_pypackage.modules as tegaki
#import hiking_tegaki_pypackage.cv as tegakicv
import math
import sys
import os
#====================================
#combine imgs to multi column imglist
#------------------------------------
#input:
#   iplimagefiles <=(tuple)
#   column_num
#====================================
def combine(images, maxcolumn):
    width=0
    height=0
    #decide combined width,height
    nowcolumn=0
    prevheight=0
    nowwidth=0
    images.sort
    for image in images:
        nowcolumn+=1
        if (nowcolumn==maxcolumn):
            prevheight=height
            nowwidth+=image.width
            if (nowwidth>width):
                width=nowwidth
            nowcolumn=0
            nowwidth=0
        else:
            nowwidth+=image.width
        
        if ((image.height+prevheight)>height):
            height=(prevheight+image.height)
            
    print "width, height",width, height
    image_target = cvCreateImage(cvSize(width, height), IPL_DEPTH_8U, 3)
    cvZero(image_target)
    cvNot(image_target, image_target)

    images.sort

    roi=cvRect(0, 0, 0, 0)
    nowcolumn=0
    nowheight=0
    for image in images:
        nowcolumn+=1
      
        print roi.x, roi.y
        roi.width=image.width
        roi.height=image.height
        sub =cvGetSubRect(image_target, roi)
        cvCopy(image, sub)

        roi.x+=image.width
        if (image.height>nowheight):
            nowheight=image.height
        if (nowcolumn==maxcolumn):
            roi.y+=nowheight
            nowcolumn=0
            roi.x=0



    return image_target

#====================================
#combine imgs to multi column imglist
#------------------------------------
#input:
#   iplimagefiles <=(tuple)
#   column_num
#====================================
def combine(images, maxcolumn):
    width=0
    height=0
    #decide combined width,height
    nowcolumn=0
    prevheight=0
    nowwidth=0
    for image in images:
        nowcolumn+=1
        nowwidth+=image.width
        if (nowwidth>width):
            width=nowwidth
        

        if (image.height+prevheight>height):
            height=prevheight+image.height
        if (nowcolumn==maxcolumn):
            prevheight=height
            nowcolumn=0
            nowwidth=0
            
        
            
    print "width, height",width, height
    image_target = cvCreateImage(cvSize(width, height), IPL_DEPTH_8U, 3)
    cvZero(image_target)
    cvNot(image_target, image_target)

    roi=cvRect(0, 0, 0, 0)
    nowcolumn=0
    nowheight=0
    for image in images:
        nowcolumn+=1
      
        #print roi.x, roi.y
        roi.width=image.width
        roi.height=image.height
        sub =cvGetSubRect(image_target, roi)
        cvCopy(image, sub)

        roi.x+=image.width
        if (image.height>nowheight):
            nowheight=image.height
        if (nowcolumn==maxcolumn):
            roi.y+=nowheight
            nowcolumn=0
            roi.x=0



    return image_target


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
    widthsize=1
    outputpath="temp.jpg"
    if(len(sys.argv)>=3):
        outputpath = sys.argv[2]
    if(len(sys.argv)>=4):
        widthsize = int(sys.argv[3])
    print "targetdirectory:",targetpath
    print "output:",outputpath
    print "widthsize:",widthsize

    #--------------------
    #read
    #--------------------
    filelist = os.listdir(targetpath)
    #print "list",filelist

    imagelist=[]
    for file in filelist:
        if(file.find("jpg")>0):
            imagelist.append(cvLoadImage(targetpath+"/"+file))
        elif(file.find("JPG")>0):
            imagelist.append(cvLoadImage(targetpath+"/"+file))
        elif(file.find("png")>0):
            imagelist.append(cvLoadImage(targetpath+"/"+file))
    #print "imagelist",imagelist


    #image_combined = tegakicv.combine_onecolumn(imagelist)
    image_combined = combine(imagelist, widthsize)
    cvSaveImage( outputpath, image_combined)

    exit(0)
