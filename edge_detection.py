import numpy as np
import matplotlib.pyplot as plt
import skimage as sk
import neighbourhood_operations as n_o

def edgebinary(img,wind,hist=False,thershold=4):
  # return binary image depicting edges
  edgim=n_o.conv2d(img,wind,padding='mirror')
  thers=np.histogram(img.flatten())[1][thershold]
  if(hist):
    plt.hist(img.flatten())
    plt.axvline(thers,label='thershold')
  return np.round(np.asarray(edgim>thers)).astype('uint8')