# -*- coding: utf-8 -*-
"""Line.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c-PtsmmEBdysbi-9Urx63pTqnNLRxocZ
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

plt.axis([-3,6,-3,6])

plt.axis('on')
plt.grid(True)

 A = np.array([[3,-4],
 [3, 1]])
 B = np.array([-6,9]) 
 P = np.linalg.solve(A, B) 

 C = np.array([[3,-4],
 [0, 1]])
 D = np.array([-6,0]) 
 Q = np.linalg.solve(C, D) 

 E = np.array([[3,1],
 [0, 1]])
 F = np.array([9,0]) 
 R = np.linalg.solve(E, F) 

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

  #Generating all lines
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RP = line_gen(R,P)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RP[0,:],x_RP[1,:],label='$RS$')

tri_coords = np.vstack((P,Q,R)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['P','Q','R']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center


plt.savefig('line.pdf')
plt.show()