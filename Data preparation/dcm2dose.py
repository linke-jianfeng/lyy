import pydicom 
import matplotlib.pyplot as plt
import matplotlib
import scipy.misc 
import pandas as pd
import numpy as np
import os 
import pydicom as dc
import pylab
import numpy
import scipy.misc
from PIL import Image
import matplotlib.image as mpimg
import numpy as np
from skimage import data,img_as_float
import skimage.io as io

ds=dc.read_file('RTDOSE_1.2.826.0.1.3680043.2.200.870080868.762.11732.2743.dcm')

piexl_bytes=ds.PixelData

pix=ds.pixel_array

pix=pix
print(np.max(pix))
k=0
dst=img_as_float(pix)*2
print(np.max(dst))
print(np.min(dst))
print(dst.dtype.name)

#for i in dst:
 #   out_path = "C:/Users/刘耀颖/Desktop/70例NPC-20200202/'/dose1/"+str(k)+".png"
  #  io.imsave(out_path,i)
  #  k=k+1
#im = Image.fromarray(pix[50])
#out_path = "C:/Users/刘耀颖/Desktop/3dunet/2d/数据准备/png/dose/1/"+str(k)+".jpg"
#im.save(out_path)
#img = mpimg.imread('50.png')
#print(np.max(img))


