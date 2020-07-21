# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 09:05:57 2020

@author: hedelu
"""

import cv2
print(cv2.__version__)
videoCapture = cv2.VideoCapture('D:/python_test/pycharm_test/xx.mp4')
 
fps = 25 #保存视频的帧率
size = (1920,1080) #保存视频的大小
 
videoWriter =cv2.VideoWriter('D:/python_test/pycharm_test/xx2_20.mp4',cv2.VideoWriter_fourcc('m','p','4','v'),fps,size)
#videoWriter =cv2.VideoWriter('video4.avi',cv2.VideoWriter_fourcc('X','V','I','D'),fps,size)
i = 0
 
while True:
    success,frame = videoCapture.read()
    if success:
        i += 1
        print('i = ',i)
        if(i>=50 and i <= 500):
            videoWriter.write(frame)
        #elif i >1400:
        #    break
    else:
        print('end')   
        break
videoWriter.release()