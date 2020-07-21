# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 15:24:12 2020
找摄像头是哪个代号
海康相机rtsp拉流视频显示
@author: hedelu
"""

#import cv2
#ID = 0
#while(1):
#    cap = cv2.VideoCapture(ID)
#    # get a frame
#    ret, frame = cap.read()
#    if ret == False:
#        ID += 1
#        print(ID)
#    else:
#        print(ID)
#        break

import cv2
cap = cv2.VideoCapture("rtsp://admin:haikangcrrc1@192.168.1.64:554/h264/ch1/main/av_stream")
ret, frame = cap.read()
while ret:
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
