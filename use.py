import numpy as np
import matplotlib.pyplot as plt
import skimage as sk


# Usefull Functions
def imshow(image,size=(10,10),mode='gray',title=None):
  # display a grayscale image 
  plt.figure(figsize=size)
  plt.title(title)
  plt.axis('off')
  plt.imshow(image,cmap=mode)
  plt.show()

 
def showhimgs(ims,size=(18,14),mode='gray',titles=None,axes=False):
  # display grayscale images passed in list img horizontally 
  nimgs=len(ims)
  fig,axs=plt.subplots(1,nimgs,figsize=size)
  for i in range(nimgs):
    if(axes!=True): axs[i].axis('off')
    axs[i].imshow(ims[i],cmap=mode)
    if(titles):
      axs[i].set_title(titles[i])
  plt.show()


def showvimgs(ims,size=(18,14),mode='gray',titles=None,axes=False):
    # display grayscale images passed in list img vertically 
  nimgs=len(ims)
  fig,axs=plt.subplots(nimgs,1,figsize=size)
  for i in range(nimgs):
    if(axes!=True): axs[i].axis('off')
    axs[i].imshow(ims[i],cmap=mode)
    if(titles): 
      axs[i].set_title(titles[i])
  plt.show()

def load_gray_image(file):
  # load a grayscale image with pixel values in range 0 to 255
  # returned image pixe values of type float, if type uint8 desired, do image.astype('uint8')
  image=sk.io.imread(file)
  image=sk.color.rgb2gray(image)*255
  return image


def random_matrix(shape):
  # returns a matrix of random integers in the ragne (0,9) for a given shape
  # shape must be a tuple!
  return (np.random.rand(*shape)*10).astype('int')

def dec2bin(num):
  out='1'
  while(num>1):
    out+=str(num%2)
    num=num//2 
  return out[::-1]