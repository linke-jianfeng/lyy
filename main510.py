from model3 import *
from datanew import *
import matplotlib.pyplot as plt
#os.environ["CUDA_VISIBLE_DEVICES"] = "0"


data_gen_args = dict(rotation_range=0.2,
                    width_shift_range=0.2,
                    height_shift_range=0.2,
                    shear_range=0.05,
                    zoom_range=0.05,
                    horizontal_flip=True,
                    fill_mode='nearest')
myGene = trainGenerator(8,'/gs/home/liuyaoying/256dose_prediction/data/membrane/train','image','label',data_gen_args,save_to_dir = None)
validation =validationGenerator(8,'/gs/home/liuyaoying/256dose_prediction/data/v/train','image','label',save_to_dir = None)



model = unet()
model_checkpoint = ModelCheckpoint('510.hdf5', monitor='loss',verbose=2, save_best_only=True)
history=model.fit_generator(myGene,steps_per_epoch=627,epochs=300,
                    callbacks=[model_checkpoint],
                    validation_data=validation,
                    validation_steps=62,
                    verbose=2)

loss=history.history['loss']
val_loss=history.history['val_loss']

epochs=range(1,len(loss)+1)

plt.plot(epochs,loss,'bo',label='Training loss')
plt.plot(epochs,val_loss,'b',label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.savefig("filename.png")





