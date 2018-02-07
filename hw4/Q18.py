import math
import numpy as np

def readin_data():
  with open('train.txt') as file:
    lines = [line.split() for line in file]
  data = []
  datax = []
  datay = []
  for line in lines:
    tmp = []
    tmp.append(1.0)
    for i in line:
      tmp.append(float(i))
    data.append(tmp)
    datax.append(tmp[0:-1])
    datay.append(tmp[-1])
  return np.asmatrix(data) , np.asmatrix(datax) , datay

def readin_testdata():
  with open('test.txt') as file:
    lines = [line.split() for line in file]
  data = []
  datax = []
  datay = []
  for line in lines:
    tmp = []
    tmp.append(1.0)
    for i in line:
      tmp.append(float(i))
    data.append(tmp)
    datax.append(tmp[0:-1])
    datay.append(tmp[-1])
  return np.asmatrix(data) , np.asmatrix(datax) , datay

def sign(x):
  if x > 0.0:
    return 1
  else:
    return -1

def gradient(x , y , lamda):
  y = np.asmatrix(y)
  lamdaI = lamda * np.identity(x.shape[1])
  inverse = np.linalg.inv(np.dot(x.transpose() , x) + lamdaI)
  return np.dot( np.dot( inverse , x.transpose() ) , y.transpose() )

def count_error(W , x , y , size):
  counter = 0.0
  for i in range(size):
    mat = np.dot(x[i] , W)
    if sign(mat) != y[i]:
      counter += 1
  return counter / size

train_data , train_datax , train_datay = readin_data()
test_data , test_datax , test_datay = readin_testdata()
Wreg = gradient(train_datax , train_datay , 1.0)
Ein = count_error(Wreg , train_datax , train_datay , len(train_data))
Eout = count_error(Wreg , test_datax , test_datay , len(test_data))

print Ein , Eout