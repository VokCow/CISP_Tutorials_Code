import numpy as np

# delta=10/256
def dec2bin(num):
  out=[1]
  while(num>1):
    out.append(num%2)
    num=num//2 
  return out[::-1]

def imquantize(img,bks,M):
  Out = np.zeros_like(img)
  if M==8: print(bks)
  for i in range(1,M):
    Out+=((img>bks[i-1])*(img<=bks[i])*i).astype('uint8')
  Out+=((img>bks[i])*i).astype('uint8')
  # calculate mean square error
  rows,cols=img.shape
  MSE=1/(rows*cols)*((Out-img)**2).sum()
  return Out,MSE

def uniform(img,M):
  values=np.arange(img.min(),img.max())
  delta=len(values)//(M)
  bks=values[::delta]
  out,MSE=imquantize(img,bks,M)

  bpp=len(dec2bin(M))
  PSNR=20*np.log10(M)-10*np.log10(MSE) # source https://en.wikipedia.org/wiki/Peak_signal-to-noise_ratio

  print(f'For Delta: {delta}, M: {M}, MSE: {MSE} bpp: {bpp} PSNR: {PSNR}')
  return out,bpp,PSNR,MSE
