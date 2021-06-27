# -*- coding: utf-8 -*-
"""Line.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c-PtsmmEBdysbi-9Urx63pTqnNLRxocZ
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as LA

#import math
#from coeffs import *
import subprocess
import shlex


#generating the line points
def line_gen(A,B):
	len = 20
	dim = A.shape[0]
	x_AB = np.zeros((dim,len))
	lam_1 = np.linspace(0,1,len)
	for i in range(len):
		temp1 = A + lam_1[i]*(B-A)
		x_AB[:,i]=temp1.T
	return x_AB

#vertices
P = np.array([6,6])
Q= np.array([-2,0])
R = np.array([0, 9])
S = np.array([3, 0])

#Direction vectors
print(P-S, R-S, Q-S)

#Side lengths
print(LA.norm(R-S), LA.norm(Q-P), LA.norm(Q-S))


#Generating the lines
x_PQ = line_gen(P,Q)
x_RS = line_gen(R,S)
x_SQ = line_gen(S,Q)

#plotting the all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_RS[0,:],x_RS[1,:],label='$RS$')
plt.plot(x_SQ[0,:],x_SQ[1,:],label='$SQ$')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')

#Saving figures
#if using termux
plt.savefig('line.pdf')
#else
plt.show()