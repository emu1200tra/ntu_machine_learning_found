import numpy as np
import random
import math
from matplotlib import pyplot as plt

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

#Q18
data , datax , datay = readin_data()
test_data , test_datax , test_datay = readin_testdata()
T = 2000

for eta in [0.01 , 0.001]:

  w = [0.0 for i in range(len(datax[0]))]
  w = np.asarray(w)
  w = np.asmatrix(w)
  Ein_record = []
  testEin_record = []

  counter = 0.0
  for j in range(len(data)):
    test_xn = np.asmatrix(np.asarray(datax[j]))
    wt = w.transpose()
    flag = np.dot(test_xn , wt)
    if sign(flag) != datay[j]:
      counter += 1.0
  Ein_record.append(counter / len(data))

  #Eout
  counter = 0.0
  for j in range(len(test_data)):
    test_xn = np.asmatrix(np.asarray(test_datax[j]))
    wt = w.transpose()
    flag = np.dot(test_xn , wt)
    if sign(flag) != test_datay[j]:
      counter += 1.0
  testEin_record.append(counter / len(test_data))

  for i in range(T):
    
    #Ein
    w = w-eta*gradient(w , datax , datay)
    counter = 0.0
    for j in range(len(data)):
      test_xn = np.asmatrix(np.asarray(datax[j]))
      wt = w.transpose()
      flag = np.dot(test_xn , wt)
      if sign(flag) != datay[j]:
        counter += 1.0
    Ein_record.append(counter / len(data))

    counter = 0.0
    for j in range(len(test_data)):
      test_xn = np.asmatrix(np.asarray(test_datax[j]))
      wt = w.transpose()
      flag = np.dot(test_xn , wt)
      if sign(flag) != test_datay[j]:
        counter += 1.0
    testEin_record.append(counter / len(test_data))

  plt.subplot(1 , 2 , 1)
  plt.plot(range(1 , len(Ein_record)+1) , Ein_record , label = "GD")
  plt.subplot(1 , 2 , 2)
  plt.plot(range(1 , len(testEin_record)+1) , testEin_record , label = "GD")
  
  counter1 = 0.0
  counter2 = 0.0
  for i in range(len(Ein_record)):
    counter1 += Ein_record[i]
    counter2 += testEin_record[i]

  print "GD Ein" , counter1 / len(Ein_record)
  print "GD Eout" , counter2 / len(testEin_record)


  #Q20
  w = [0.0 for i in range(len(datax[0]))]
  w = np.asarray(w)
  w = np.asmatrix(w)
  Ein_record = []
  testEin_record = []
  counter = 0.0
  for j in range(len(data)):
    test_xn = np.asmatrix(np.asarray(datax[j]))
    wt = w.transpose()
    flag = np.dot(test_xn , wt)
    if sign(flag) != datay[j]:
      counter += 1.0
  Ein_record.append(counter / len(data))

  counter = 0.0
  for j in range(len(test_data)):
    test_xn = np.asmatrix(np.asarray(test_datax[j]))
    wt = w.transpose()
    flag = np.dot(test_xn , wt)
    if sign(flag) != test_datay[j]:
      counter += 1.0
  testEin_record.append(counter / len(test_data))

  for i in range(T):
    n = i % len(datax)
    xn = np.asmatrix(np.asarray(datax[n]))
    yn = np.asmatrix(np.asarray(datay[n]))
    xn = xn.transpose()
    s = -(np.dot(np.dot(w , xn) , yn))  
    xn = xn.transpose()
    w = w+eta*sigmoid(s)*(np.dot(yn , xn))

    counter = 0.0
    for j in range(len(data)):
      test_xn = np.asmatrix(np.asarray(datax[j]))
      wt = w.transpose()
      flag = np.dot(test_xn , wt)
      if sign(flag) != datay[j]:
        counter += 1.0
    Ein_record.append(counter / len(data))

    counter = 0.0
    for j in range(len(test_data)):
      test_xn = np.asmatrix(np.asarray(test_datax[j]))
      wt = w.transpose()
      flag = np.dot(test_xn , wt)
      if sign(flag) != test_datay[j]:
        counter += 1.0
    testEin_record.append(counter / len(test_data))

  plt.subplot(1 , 2 , 1)
  plt.plot(range(1 , len(Ein_record)+1) , Ein_record , label = "SGD")
  plt.xlabel("T(with lr=" + str(eta) + ")")
  plt.ylabel("Ein\n(blue for GD and orange for SGD)")
  plt.subplot(1 , 2 , 2)
  plt.plot(range(1 , len(testEin_record)+1) , testEin_record , label = "SGD")
  plt.xlabel("T(with lr=" + str(eta) + ")")
  plt.ylabel("Eout\n(blue for GD and orange for SGD)")
  plt.tight_layout()
  plt.show()

  counter1 = 0.0
  counter2 = 0.0
  for i in range(len(Ein_record)):
    counter1 += Ein_record[i]
    counter2 += testEin_record[i]

  print "SGD Ein" , counter1 / len(Ein_record)
  print "SGD Eout" , counter2 / len(testEin_record)

