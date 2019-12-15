import copy
import matplotlib.pyplot as plt
import numpy as np


'''
Implementation of Huffman encoder
'''
def lowest_pair(source):
  # find the lowest two less probable symbols in the source distribution
  symbols,values=np.array(list(source.keys())),np.array(list(source.values()))
  ais=symbols[np.argsort(values)]
  # print(ais[0],ais[1])
  return ais[0],ais[1]

def Huffman(source):

# all the source distribution versions will be stored in this list X
  X=[source]
  t_source=copy.deepcopy(source)

# iteratively merge the two less probable symbols until the source distribution consist in only two symbols
  while(True):
    
    a1,a2=lowest_pair(t_source)
    # print(t_source)
    # print(a1,a2)
    p1,p2=t_source.pop(a1),t_source.pop(a2)
    t_source[a1+a2]=p1+p2

    X.append(t_source)
    t_source=copy.deepcopy(t_source)

    if len(t_source)==2: break

  code=dict(zip(t_source.keys(),['1','0']))

# reverse the list containing source distributions 
  X_r = X[::-1]

# reconstruct the codes starting with the symbols in the last source distribution version
  for i in range(len(X_r)-1):

    a_old=set(X_r[i].keys())-set(X_r[i+1].keys())
    a_new=set(X_r[i].keys()).symmetric_difference(set(X_r[i+1].keys()))-a_old

    # print(f'a_old: {a_old}, a_new: {a_new}')

    a_old=list(a_old)[0]
    a_new=list(a_new)
    
    # check that reconstruction is done in proper order
    if a_old[0] == a_new[0]:
      a1,a2=a_new[0],a_new[1]
    else:
      a1,a2=a_new[1],a_new[0]

    # print(f'a_old: {a_old}, a1: {a1} a2: {a2}')

    code_old=code.pop(a_old)
    code[a1]=code_old + '1'
    code[a2]=code_old + '0'

  return  code

def encoder(arr,code):
  out=np.zeros_like(arr).astype('<U6')
  for symbol,cod in code.items():
    idxs=np.argwhere(arr==symbol)
    out[idxs.flatten()]=cod
  return out

def decoder(arr,code):
  out=np.zeros_like(arr).astype('<U6')
  for symbol,cod in code.items():
    idxs=np.argwhere(arr==cod)
    out[idxs.flatten()]=symbol
  return out

# Efficiency:
def efficiency(source):
  code=Huffman(source)
  codes,probs=list(code.values()),list(source.values())
  return sum([len(codes[i])*probs[i] for i in range(len(codes))])

def entropy(probs):
  probs=np.asarray(probs)
  return (-probs*np.log2(probs)).sum()