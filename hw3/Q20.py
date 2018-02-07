import numpy as np
import random
import math

def readin_data():
  with open('train.txt') as file:
    lines = [line.split() for line in file]
  data = []
  datax = []
  datay = []
  for line in lines:
    tmp = []
    for i in line:
      tmp.append(float(i))
    data.append(tmp)
    datax.append(tmp[0:-1])
    datay.append(tmp[-1])
  return data , datax , datay

def sigmoid(s):
  return math.exp(s)/(1.0+math.exp(s))
'''
def gradient(w , x , y):
  N = len(x)
  counter = 0.0
  for i in range(N):
    xn = np.asmatrix(np.asarray(x[i]))
    yn = np.asmatrix(np.asarray(y[i]))
    xn = xn.transpose()
    s = -(np.dot(np.dot(w , xn) , yn))  
    xn = xn.transpose()
    counter += sigmoid(s)*(-1)*(np.dot(yn , xn))
  return counter / N
'''
def readin_testdata():
  with open('test.txt') as file:
    lines = [line.split() for line in file]
  data = []
  datax = []
  datay = []
  for line in lines:
    tmp = []
    for i in line:
      tmp.append(float(i))
    data.append(tmp)
    datax.append(tmp[0:-1])
    datay.append(tmp[-1])
  return data , datax , datay

def sign(x):
  if x > 0:
    return 1
  else:
    return -1

data , datax , datay = readin_data()
T = 2000
eta = 0.001
w = [0.0 for i in range(len(datax[0]))]
w = np.asarray(w)
w = np.asmatrix(w)
print len(datax)
for i in range(T):
  n = i % len(datax)
  xn = np.asmatrix(np.asarray(datax[n]))
  yn = np.asmatrix(np.asarray(datay[n]))
  xn = xn.transpose()
  s = -(np.dot(np.dot(w , xn) , yn))  
  xn = xn.transpose()
  w = w+eta*sigmoid(s)*(np.dot(yn , xn))
  #print w.shape , np.dot(yn , xn).shape

test_data , test_datax , test_datay = readin_testdata()

counter = 0.0
for i in range(len(test_data)):
  test_xn = np.asmatrix(np.asarray(test_datax[i]))
  wt = w.transpose()
  flag = np.dot(test_xn , wt)
  if sign(flag) != test_datay[i]:
    counter += 1.0

print counter / len(test_data)