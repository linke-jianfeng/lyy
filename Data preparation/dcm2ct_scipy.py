import pydicom 
import matplotlib.pyplot as plt 
import scipy.misc 
import pandas as pd
import numpy as np
import os
from PIL import Image
import matplotlib.image as mpimg
from skimage import data,img_as_float
import skimage.io as io
import matplotlib.image as mpimg

def Dcm2jpg(file_path):
    #获取所有图片名称
    c = []
    names = os.listdir(file_path)  #路径
    #将文件夹中的文件名称与后边的 .dcm分开
    for name in names:
        index = name.rfind('.')
        name = name[:index]
        c.append(name)
    k=int(1)
    for files in c :
        picture_path = "C:/Users/刘耀颖/Desktop/70例NPC-20200202/70/"+files+".dcm"
        out_path ="C:/Users/刘耀颖/Desktop/70例NPC-20200202/70/"+files+".png" 
        ds = pydicom.read_file(picture_path)
        img = ds.pixel_array # 提取图像信息
        #print(np.max(img))
        #print(img.dtype.name)
        #dst=img_as_float(img)*15
        #print(np.max(img))
        #print(dst.dtype.name)
        scipy.misc.imsave(out_path,img)
        
    
    print('all is changed')
            
Dcm2jpg("C:/Users/刘耀颖/Desktop/70例NPC-20200202/70")

#img = mpimg.imread('C:/Users/刘耀颖/Desktop/新建文件夹/CT_1.2.826.0.1.3680043.2.200.864857431.585.64337.1276.15.png')
#print(np.max(img))





