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
a=np.zeros((34,256,256))
print(a.shape)
for i in range(0,82):
    img = mpimg.imread('2/'+str(i)+'_predict.png')
    img=img[np.newaxis,:]
    a=np.vstack((a,img))
    #print(a.shape)
for i in range(0,57):
    d=np.zeros((1,256,256))
    a=np.vstack((a,d))
    #print(a.shape)

a=a*32574
a=a.astype(int)
print(np.max(a))
print(a.dtype)
b=a.astype(np.uint16)
print(b.dtype)
print(np.max(b))
ds=dc.read_file('RTDOSE_1.2.826.0.1.3680043.2.200.635117546.529.41176.763.dcm')
print(ds.pixel_array.dtype)
ds.PixelData=b.tobytes()
ds.save_as('NEW_ExplVR_BigEnd.dcm')
