import random
import math
import numpy as np

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

def check(x1 , x2 , y):
  result1 = sign_(-1.0-0.05*x1+0.08*x2+0.13*x1*x2+15*x1**2+1.5*x2**2)
  result2 = sign_(-1.0-0.05*x1+0.08*x2+0.13*x1*x2+1.5*x1**2+15*x2**2)
  result3 = sign_(-1.0-1.5*x1+0.08*x2+0.13*x1*x2+0.05*x1**2+1.5*x2**2)
  result4 = sign_(-1.0-0.05*x1+0.08*x2+0.13*x1*x2+1.5*x1**2+1.5*x2**2)
  result5 = sign_(-1.0-1.5*x1+0.08*x2+0.13*x1*x2+0.05*x1**2+0.05*x2**2)
  return result1*y , result2*y , result3*y , result4*y , result5*y

err_counter = 0.0
list_record = [0 , 0 , 0 , 0 , 0]
for index in range(1000):
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
  for i in range(len(data_list)):
    #print Wlin.shape , datax[i].shape
    flag = np.dot(datax[i] , Wlin)
    #print flag
    '''
    if sign_(flag) != datay[i][0]:
      err_counter += 1
    '''
    result = [0 , 0 , 0 , 0 , 0]
    result[0] , result[1] , result[2] , result[3] , result[4] = check(datax_original[i][1] , datax_original[i][2] , sign_(flag))
    for j in range(5):
      if result[j] > 0:
        list_record[j] += 1

print err_counter / (1000*1000)
print list_record