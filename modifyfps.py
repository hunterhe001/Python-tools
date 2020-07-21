# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:26:54 2020
改视频帧率
@author: hedelu
"""

from moviepy.editor import *
clip = VideoFileClip('D:/西交__前视障碍物/视频抽帧及对齐/bwv_rec.mp4')
clip.write_videofile('D:/西交__前视障碍物/视频抽帧及对齐/bwv_rec_25fps.mp4', fps=25)
#clip.reader.close()