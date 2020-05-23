import os
import sys
import re
g=input("序号是：")
def rename():
    path=("C:/Users/刘耀颖/Desktop/256dose_prediction/test/510/TEST/"+str(g)+"/1")
    startNumber=input("起始数字:")
    fileType=(".png")
    print("正在生成以"+startNumber+fileType+"迭代的文件名")
    count=0
    filenames=os.listdir(path)
    filenames.sort(key=lambda x:int(x[:-4]))
    for files in filenames:
        Olddir=os.path.join(path,files)
        if os.path.isdir(Olddir):
            continue
        Newdir=os.path.join(path,str(count+int(startNumber))+fileType)
        os.rename(Olddir,Newdir)
        count+=1
    print("一共修改了"+str(count)+"个文件")

    path=("C:/Users/刘耀颖/Desktop/256dose_prediction/test/510/TEST/"+str(g)+"/2")
    fileType=(".png")
    print("正在生成以"+startNumber+fileType+"迭代的文件名")
    count=0
    filenames=os.listdir(path)
    filenames.sort(key=lambda x:int(x[:-4]))
    for files in filenames:
        Olddir=os.path.join(path,files)
        if os.path.isdir(Olddir):
            continue
        Newdir=os.path.join(path,str(count+int(startNumber))+fileType)
        os.rename(Olddir,Newdir)
        count+=1
    print("一共修改了"+str(count)+"个文件")
    
rename()
#path=("C:/Users/刘耀颖/Desktop/701/VALIDATION/"+str(g)+"/2")
#filenames=os.listdir(path)
#filenames.sort(key=lambda x:int(x[:-4]))
#print(filenames)
