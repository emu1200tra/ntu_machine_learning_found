import math
import numpy as np
import random
from matplotlib import pyplot as plt

def readin_data():
  with open('train.txt') as file:
    lines = [line.split() for line in file]
  data = []
  traindatax = []
  traindatay = []
  valdatax = []
  valdatay = []
  counter = 0
  for line in lines:
    if counter < 120:
      tmp = []
      tmp.append(1.0)
      for i in line:
        tmp.append(float(i))
      data.append(tmp)
      traindatax.append(tmp[0:-1])
      traindatay.append(tmp[-1])
    else:
      tmp = []
      tmp.append(1.0)
      for i in line:
        tmp.append(float(i))
      data.append(tmp)
      valdatax.append(tmp[0:-1])
      valdatay.append(tmp[-1])
    counter += 1
  return np.asmatrix(data) , np.asmatrix(traindatax) , traindatay , np.asmatrix(valdatax) , valdatay

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

def lamda_generate():
  lamda = []
  for i in range(-10 , 3):
    lamda.append(math.pow(10 , i))
  return lamda

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

train_data , train_datax , train_datay , valdatax , valdatay = readin_data()
test_data , test_datax , test_datay = readin_testdata()
lamda = lamda_generate()
minEtrain = 1.0
recordlamda = 0.0
recordEval = 0.0
recordEout = 0.0
Etrain_list = []
minval = 1.0
recordEout2 = 0.0
recordEtrain = 0.0
recordlamda2 = 0.0
Eval_list = []
for i in lamda:
  Wreg = gradient(train_datax , train_datay , i)
  Etrain = count_error(Wreg , train_datax , train_datay , len(train_datax))
  Eval = count_error(Wreg , valdatax , valdatay , len(valdatax))
  Eout = count_error(Wreg , test_datax , test_datay , len(test_data))
  if Etrain <= minEtrain:
    recordlamda = math.log(i , 10)
    recordEval = Eval
    recordEout = Eout
    minEtrain = Etrain
  if Eval <= minval:
    recordlamda2 = math.log(i , 10)
    recordEtrain = Etrain
    recordEout2 = Eout
    minval = Eval
  Etrain_list.append(Etrain)
  Eval_list.append(Eval)

print recordlamda , recordEval , recordEout , minEtrain

print recordlamda2 , recordEtrain , recordEout2 , minval

for i in range(len(lamda)):
  lamda[i] = math.log(lamda[i] , 10)

plt.plot(lamda , Etrain_list)
plt.plot(lamda , Eval_list)
plt.xlabel("lamda")
plt.ylabel("Etrain(Blue):Eval(Orange)")
plt.show()