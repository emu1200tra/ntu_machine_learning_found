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
  return data , datax , datay

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
minEcv = 1.0
recordlamda = 0.0

for i in lamda:
  Ecv = 0.0
  for j in range(len(train_data) / 40):
    cvtraindatax = []
    cvtraindatay = []
    cvtraindatax = train_datax[0:40*j] + train_datax[40*(j+1):]
    cvtraindatay = [train_datay[0:40*j] + train_datay[40*(j+1):]]
    cvtestdatax = train_datax[40*j:40*(j+1)]
    cvtestdatay = train_datay[40*j:40*(j+1)]
    Wreg = gradient(np.asmatrix(cvtraindatax) , cvtraindatay , i)
    Ecv += count_error(Wreg , cvtestdatax , cvtestdatay , len(cvtestdatax))
  totalEcv = Ecv / (len(train_data) / 40)
  if totalEcv <= minEcv:
    minEcv = totalEcv
    recordlamda = math.log(i , 10)

print minEcv , recordlamda

train_data , train_datax , train_datay = readin_data()
test_data , test_datax , test_datay = readin_testdata()
Wreg = gradient(np.asmatrix(train_datax) , train_datay , math.pow(10 , recordlamda))
Ein = count_error(Wreg , train_datax , train_datay , len(train_data))
Eout = count_error(Wreg , test_datax , test_datay , len(test_data))

print Ein , Eout