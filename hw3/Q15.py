import random
import math
import numpy as np
from matplotlib import pyplot as plt

def sign(x1 , x2):
  if x1**2 + x2**2 - 0.6 > 0:
    return 1
  else:
    return -1

def sign_(x):
  if x > 0:
    return 1
  else:
    return -1

def generate_noise(data_list):
  index = range(1000)
  random.shuffle(index)
  noise_data = []
  for i in range(100):
    noise_data.append([1 , data_list[index[i]][1] , data_list[index[i]][2] , -data_list[index[i]][3]])
  return data_list + noise_data

def generate_data():
  data_list = []
  for i in range(1000):
    x1 = random.uniform(-1 , 1)
    x2 = random.uniform(-1 , 1)
    data_list.append([1 , x1 , x2 , sign(x1 , x2)])
  return data_list

def data_derive(data_list):
  datax = []
  datay = []
  for i in range(len(data_list)):
    datax.append([1 , data_list[i][1] , data_list[i][2]])
    datay.append(data_list[i][3])
  return datax , datay

def projection(datax):
  new_data = []
  for i in range(len(datax)):
    new_data.append([1 , datax[i][1] , datax[i][2] , datax[i][1]*datax[i][2] , datax[i][1]**2 , datax[i][2]**2])
  return new_data

err_counter = 0.0
counter_record = []
for index in range(1000):
  counter = 0.0
  data_list = generate_data()
  data_list = generate_noise(data_list)
  datax , datay = data_derive(data_list)
  datax_original = datax
  datax = projection(datax)
  datax = np.asarray(datax)
  datax = np.asmatrix(datax)
  datay = np.asarray(datay)
  datay = np.asmatrix(datay)
  datay = datay.transpose()
  Wlin = np.dot(np.linalg.pinv(datax) , datay)

  data_list2 = generate_data()
  data_list2 = generate_noise(data_list2)
  datax2 , datay2 = data_derive(data_list2)
  datax_original = datax2
  datax2 = projection(datax2)
  datax2 = np.asarray(datax2)
  datax2 = np.asmatrix(datax2)
  datay2 = np.asarray(datay2)
  datay2 = np.asmatrix(datay2)
  datay2 = datay2.transpose()


  for i in range(len(data_list)):
    #print Wlin.shape , datax[i].shape
    flag = np.dot(datax2[i] , Wlin)
    #print flag
    
    if sign_(flag) != datay2[i][0]:
      err_counter += 1
      counter += 1


  counter_record.append(counter/len(data_list))

print err_counter / (1000*1000)
plt.bar(range(1 , len(counter_record)+1) , counter_record)
plt.xlabel("run")
plt.ylabel("Eout")
plt.show()