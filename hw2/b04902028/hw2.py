import random
import math
from matplotlib import pyplot as plt

def sign(input_num):
  if input_num > 0:
    return 1
  else:
    return -1

def noise():
  tmp = random.randint(1 , 100)
  if tmp <= 20:
    return -1
  else:
    return 1

def generate_data():
  x = random.uniform(-1 , 1)
  noise_flag = noise()
  if noise_flag == -1:
    y = -sign(x)
  else:
    y = sign(x)

  return x , y

def generate_multidata(data_size):
  data = [[0 for i in range(2)] for j in range(data_size)]
  for i in range(data_size):
    data[i][0] , data[i][1] = generate_data()
  data.sort(key=lambda x: x[0])
  return data

def model(data , data_size):
  points = [data[0][0]] + [data[i][0] for i in range(data_size)] + [data[data_size-1][0]]
  theta_place = [(points[i+1] - points[i])/2 for i in range(data_size+1)]
  b_s = 0.0
  b_theta = 0.0
  b_Ein = 21473648
  for i in range(len(theta_place)):
    for j in [-1 , 1]:
      counter = 0.0
      for k in range(data_size):
        h_x = j * sign(data[k][0] - theta_place[i])
        if h_x != data[k][1]:
          counter += 1
      Ein = counter / data_size
      if Ein < b_Ein:
        b_Ein = Ein
        b_theta = theta_place[i]
        b_s = j
  Eout = 0.5+0.3*b_s*(abs(b_theta)-1)

  return b_Ein , Eout



data_size = input("size of data:")
print 'check:' , data_size

iteration = input("times of iteration:")
count_Ein = 0.0
count_Eout = 0.0
record_Ein = []
record_Eout = []
for i in range(iteration):
  data = generate_multidata(data_size)
  Ein , Eout = model(data , data_size)
  count_Ein += Ein
  count_Eout += Eout
  record_Ein.append(Ein)
  record_Eout.append(Eout)

plt.scatter(record_Ein , record_Eout)
plt.xlabel('Ein')
plt.ylabel('Eout')
plt.show()

print "average_Ein:" , float(count_Ein/iteration) , "; average_Eout:" , count_Eout/iteration




 
