#coding:utf-8
from hyperlpr import *
import cv2
import time
import os
import argparse
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple hyperlpr==0.0.1
def accordingtoP(elem):
    return elem[1]
def searchfolder(PATH="."):    
    dirs=os.listdir(PATH)
    success=0
    total=0
    for img in dirs:
        if img.endswith(('.jfif','.jpeg','.jpg','.png')):
            total+=1
            #print(img)
            image = cv2.imread(PATH+'/'+img)
            height=len(image)
            width=len(image[0])
            start=time.clock()
            #image=image[int(0.25*height):int(0.6*height),int(0.4*width):int(0.9*width)]#crop
            #rotate
            (h, w) = image.shape[:2] #10
            center = (w // 2, h // 2) #11
            M = cv2.getRotationMatrix2D(center, 12, 1.0) #逆时针旋转12度
            rotated = cv2.warpAffine(image, M, (w, h)) 
            #cv2.imshow("Rotated", rotated) #14
            #cv2.waitKey(0)
            #识别结果
            Result=HyperLPR_PlateRecogntion(rotated)
            elapsed = (time.clock() - start)
            if Result:
                success+=1
            if len(Result)>1:
                Result.sort(key=accordingtoP,reverse=True)        
            print("Image Name:",img,"Result:",Result,"Time elapsed:%.1fms"%(elapsed*1000))
    print("Success Num:",success,'/',total)
def detImg(PATH="E:/JYdata/chepai/00010003378000000mp4/11.jpg"):
    image = cv2.imread(PATH)
    height=len(image)
    width=len(image[0])
    image=image[int(0.25*height):int(0.6*height),int(0.4*width):int(0.9*width)]
    #image = cv2.resize(image, (0, 0), fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    #cv2.imshow('1',image)
    #cv2.waitKey(0)
    Result=HyperLPR_PlateRecogntion(image)
    print("Image Name:",PATH,"Result:",Result)

#detImg()
parser = argparse.ArgumentParser()
parser.add_argument('--folder', help='pictures folder',type=str)
parser.add_argument('--image', help='full path to image',type=str)
args = parser.parse_args()
if args.folder is not None:
    searchfolder(args.folder)
elif args.image is not None:
    detImg(args.image)
else:
    print("Please input args,--folder/--image")