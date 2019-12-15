import numpy as np
import matplotlib.pyplot as plt
import skimage as sk
import copy

def Hough_circles(img,R,steps=360):
  xs,ys=img.shape
  idxs=np.asarray(img.nonzero()) # edge pixels coordinates
  cost,sint=np.cos(np.linspace(0,2*np.pi,steps)),np.sin(np.linspace(0,2*np.pi,steps)) # cost sint coordinates
  if(isinstance(R,list)==False):
    R=[R]
  HS=np.zeros((len(R),xs,ys))
   # cosntruct size matrix
  sizeMatrix = np.ones((2,idxs.shape[1],steps))
  sizeMatrix[0,:,:] = xs
  sizeMatrix[1,:,:] = ys
  # construct zeros matrix
  zerosMatrix = np.zeros((2,idxs.shape[1],steps))
  
  for i in range(len(R)):
    d=np.asarray((R[i]*cost,R[i]*sint)) # cosine, sine matrix
    # possible circle points are constructed with input image coordinates and circle equation
    # the input image coordinates are stored in idxs and the circle equation part is stored at d 
    # we add those two contributions using a boradcasted sum, and round it changing type to 'int'
    circle_candidates = (idxs[:,:,None]-d[:,None,:]).astype('int') 
    # from those posible circle points, only the ones being greater than zero and smaller than image dimensions
    # are suitable values. We perform this suitable logic using a "logic Mask"
    logic_mask= (( circle_candidates < sizeMatrix )*( circle_candidates > zerosMatrix ))
    circle_candidates*=logic_mask 
    # only suitable (i.e. non zero) elements elements in both rows and columns are of interest
    logic_mask= logic_mask[0]*logic_mask[1] 
    xss=circle_candidates[0]*logic_mask 
    yss=circle_candidates[1]*logic_mask 
    xss,yss=xss[xss>0],yss[yss>0]
    for xssi,yssi in zip(xss,yss): 
      HS[i,xssi,yssi]+=1
  return HS

def draw_circles(img,radii,centers):
# img: image in which a circle will be drawn
# radii: list or ndarray of radii of circles
# centers: list of tuples with the centers
  out=copy.copy(img)
  th=np.arange(0,181)*np.pi/180
  for r,c in zip(radii,centers):
    x0,y0=c
    xs=(x0+r*np.cos(th)).astype('int')
    ys_p=(y0+r*np.sin(th)).astype('int')
    ys_m=(y0-r*np.sin(th)).astype('int')
    out[xs,ys_p]=1
    out[xs,ys_m]=1
  return out


def Hough_ellipses(img,params,steps=360):
  # params = [(a0,b0,phi0),(a1,b1,phi1),...]
  xs,ys=img.shape
  idxs=np.asarray(img.nonzero()) # edge pixels coordinates
  cost,sint=np.cos(np.linspace(0,2*np.pi,steps)),np.sin(np.linspace(0,2*np.pi,steps)) # cost sint coordinates
  if(isinstance(params,list)==False):
    params=[params]
  HS=np.zeros((len(params),xs,ys))
  # cosntruct size matrix
  sizeMatrix = np.ones((2,idxs.shape[1],steps))
  sizeMatrix[0,:,:] = xs
  sizeMatrix[1,:,:] = ys
  # construct zeros matrix
  zerosMatrix = np.zeros((2,idxs.shape[1],steps))
  for i in range(len(params)):
    a,b,phi=params[i]
    d=np.asarray((a*cost*np.cos(phi)-b*sint*np.sin(phi),a*cost*np.sin(phi)+b*sint*np.cos(phi)))
    # possible circle points are constructed with input image coordinates and circle equation
    # the input image coordinates are stored in idxs and the circle equation part is stored at d 
    # we add those two contributions using a boradcasted sum, and round it changing type to 'int'
    ellipse_candidates = (idxs[:,:,None]-d[:,None,:]).astype('int') 
    # from those posible circle points, only the ones being greater than zero and smaller than image dimensions
    # are suitable values. We perform this suitable logic using a "logic Mask"
    logic_mask= (( ellipse_candidates < sizeMatrix )*( ellipse_candidates > zerosMatrix ))
    ellipse_candidates*=logic_mask 
    # only suitable (i.e. non zero) elements elements in both rows and columns are of interest
    logic_mask= logic_mask[0]*logic_mask[1] 
    xss=ellipse_candidates[0]*logic_mask 
    yss=ellipse_candidates[1]*logic_mask 
    xss,yss=xss[xss>0],yss[yss>0]
    for xssi,yssi in zip(xss,yss): 
      HS[i,xssi,yssi]+=1
  return HS

def draw_ellipses(img,params):
  # params = [(x0,y0,a0,b0,phi0),(a1,b1,phi1),...]
  out=copy.copy(img)
  th=np.arange(0,181)*np.pi/180
  for param in params:
    x0,y0,a,b,phi=param
    xs_p=(x0+a*np.cos(th)*np.cos(phi)-b*np.sin(th)*np.sin(phi)).astype('int')
    ys_p=(y0+a*np.cos(th)*np.sin(phi)+b*np.sin(th)*np.cos(phi)).astype('int')
    xs_m=(x0+a*np.cos(th)*np.cos(phi)+b*np.sin(th)*np.sin(phi)).astype('int')
    ys_m=(y0+a*np.cos(th)*np.sin(phi)-b*np.sin(th)*np.cos(phi)).astype('int')
    out[xs_p,ys_p]=1
    out[xs_m,ys_m]=1
  return out

