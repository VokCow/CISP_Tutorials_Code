import numpy as np
import matplotlib.pyplot as plt
import skimage as sk


def conv2d(img,wind,padding='zeros'):
  '''
  This convolution function allows to choose which value to be used in the padding
  regions. When conv2d is used for average filters, the padding value can be safely set to zero,
  but in the case of gradient kernels, it is convenient to mirror the image at the padding regions.
  '''
  n=len(wind)
  if(padding=='zeros'):
    pad_value=0
  else:
    pad_value=1
  # In the case the kernel passed is not of odd length, padd it 
  if(n%2==0):
    pwind=pad_value*np.ones((wind.shape[0]+1,wind.shape[1]+1))
    pwind[:-1,:-1]=wind
    wind=pwind
    n+=1
    del pwind
  rows,cols=img.shape
  pimg=np.zeros((rows+n-1,cols+n-1))
  idx=n//2
  pimg[idx:-idx,idx:-idx]=img

  # padd with mirror values instead of zeros if required
  if(padding=='mirror'):
    print('mirror mode on')
    pimg[idx:-idx,:idx]=img[:,:idx]  # every firsts raws (but the corners)
    pimg[:idx,idx:-idx]=img[:idx,:] # every firsts columns (but the corners)
    pimg[idx:-idx,-idx:]=img[:,-idx:] # every lasts rows (but the corners)
    pimg[-idx:,idx:-idx]=img[-idx:,:] # every lasts columns (but the corners)

  # pad with ones if required
  if(padding=='ones'):
    print('ones mode on')
    pimg[:,:idx]=1  # every firsts raws
    pimg[:idx,:]=1 # every firsts columns
    pimg[:,-idx:]=1 # every lasts rows
    pimg[-idx:,:]=1 # every lasts columns

  out=np.zeros_like(img,dtype=float)
  for i in range(rows):
    for j in range(cols):
      out[i,j]=(wind*pimg[i:i+n,j:j+n]).sum()
    
  # out=(np.absolute(out)).astype('uint8')
  out=np.absolute(out)
  return out
  
def median(img,windsize):
  n=windsize
  if(n%2==0):
    n+=1
  rows,cols=img.shape
  # create padded version of the image
  pimg=np.zeros((rows+n-1,cols+n-1))
  idx=n//2
  pimg[idx:-idx,idx:-idx]=img
  # initialize output with same dimensions of the input image
  out=np.zeros_like(img,dtype=float)
  for i in range(rows):
    for j in range(cols):
      out[i,j]=np.median(pimg[i:i+n,j:j+n].flatten()) # use np.median() function for better performance
  return out
