import numpy as np 
import os
import skimage.io as io
import skimage.transform as trans
import numpy as np
from keras.models import *
from keras.layers import *
from keras.optimizers import *
from keras.callbacks import ModelCheckpoint, LearningRateScheduler
from keras import backend as keras
from datanew import *
c=input("input the model name:")
model = load_model(str(c)+'.hdf5')
a=[88,79,82,79]
b=[61,65,67,70]
for i in range(0,4):
    testGene = testGenerator("test/"+str(c)+"/TEST/"+str(b[i])+"/1",int(a[i]))
    results = model.predict_generator(testGene,int(a[i]),verbose=2)
    print(np.max(results))
    saveResult("test/"+str(c)+"/TEST/"+str(b[i])+"/2",results)

print('done')
