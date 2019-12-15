import numpy as np
import matplotlib.pyplot as plt
import skimage as sk


def get_histogram(img,bins):
  # returns histogram of an image
  img=np.asarray(img.flatten(),dtype=np.uint8) # flat and round image 
  hist=np.zeros(bins)
  for pixel in img:
    hist[pixel]+=1
  return hist

def hist_cum(hist):
  # returns normalized cumulative histogram
  bins=len(hist)-1
  N=len(hist)
  histcum=np.zeros(N)
  for k in range(N):
    histcum[k]=sum(hist[:k])
  histcum=np.asarray(histcum)
  histcum=(histcum-min(histcum))/(max(histcum)-min(histcum))
  return histcum*bins # return an numpy array