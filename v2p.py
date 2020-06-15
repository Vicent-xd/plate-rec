#coding:utf-8
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

'''获取视频信息'''
# cap=cv.VideoCapture('shanxi.mp4') #加载视频
# fps=cap.get(cv.CAP_PROP_FPS) # 获取帧率
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH)) # 获取宽度
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)) # 获取高度
# print(fps,width,height)

'''视频转图片'''
cap=cv.VideoCapture('焦仓车牌.mp4') #加载视频
isOpened=cap.isOpened()
i=0
while(isOpened):
    i=i+1
    flag,frame=cap.read()
    fileName = '%03d'%i+".jpg"
    print(fileName)
    if flag == True and i%100==0:
        cv.imwrite('%03d'%i+".jpg",frame) # 命名 图片 图片质量，此处文件名必须以图片格式结尾命名
        cv.waitKey(1)
    elif not flag:
        break
cap.release()
print('end')
