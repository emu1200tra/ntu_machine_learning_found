import math
import numpy as np
from matplotlib import pyplot as plt

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

train_data , train_datax , train_datay = readin_data()
test_data , test_datax , test_datay = readin_testdata()
lamda = lamda_generate()
print lamda
minEin = 1.0
recordlamda = 0.0
recordEin = 0.0
recordEout = 0.0
Ein_list = []
minEout = 1.0
recordEout2 = 0.0
recordEin2 = 0.0
recordlamda2 = 0.0
Eout_list = []
for i in lamda:
  Wreg = gradient(train_datax , train_datay , i)
  Ein = count_error(Wreg , train_datax , train_datay , len(train_data))
  Eout = count_error(Wreg , test_datax , test_datay , len(test_data))
  if Ein <= minEin:
    recordlamda = math.log(i , 10)
    recordEin = Ein
    recordEout = Eout
    minEin = Ein
  if Eout <= minEout:
    recordlamda2 = math.log(i , 10)
    recordEin2 = Ein
    recordEout2 = Eout
    minEout = Eout
  Ein_list.append(Ein)
  Eout_list.append(Eout)


print recordlamda , recordEin , recordEout

print recordlamda2 , recordEin2 , recordEout2

for i in range(len(lamda)):
  lamda[i] = math.log(lamda[i] , 10)

plt.plot(lamda , Ein_list)
plt.plot(lamda , Eout_list)
plt.xlabel("lamda")
plt.ylabel("Ein(Blue):Eout(Orange)")
plt.show()