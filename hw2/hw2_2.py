import random
import math
import numpy as np


def sign(input_num):
  if input_num > 0:
    return 1
  else:
    return -1

def read_data(filename):
  with open(filename) as file:
    lines = [line.split() for line in file]
  for i in range(len(lines)):
    for j in range(len(lines[0])):
      lines[i][j] = float(lines[i][j])  

  return np.array(lines)

def model(data , data_size , dimension):
  
  data = np.array(sorted(data, key=lambda x: x[dimension]))

  points = [data[0][dimension]] + [data[i][dimension] for i in range(data_size)] + [data[data_size-1][dimension]]
  theta_place = [(points[i+1] - points[i])/2 for i in range(data_size+1)]
  b_s = 0.0
  b_theta = 0.0
  b_Ein = 21473648
  for i in range(len(theta_place)):
    for j in [-1 , 1]:
      counter = 0.0
      for k in range(data_size):
        h_x = j * sign(data[k][dimension] - theta_place[i])
        if h_x != data[k][len(data[0])-1]:
          counter += 1
      Ein = counter / data_size
      if Ein < b_Ein:
        b_Ein = Ein
        b_theta = theta_place[i]
        b_s = j
  Eout = 0.5+0.3*b_s*(abs(b_theta)-1)

  return b_Ein , Eout , b_s , b_theta

def testing(test_data , s , theta , data_size , dimension):
  counter = 0.0
  for k in range(data_size):
    h_x = s * sign(test_data[k][dimension] - theta)
    if h_x != test_data[k][len(data[0])-1]:
      counter += 1
  Eout = counter / data_size  
  return Eout



filename = "hw2_training_data.txt"
data = read_data(filename)

record = []
minEin = 21473648
dim = 0

for i in range(len(data[0])-1):
  record.append(model(data , len(data) , i))
  if record[i][0] < minEin:
    minEin = record[i][0]
    dim = i

print record[dim]

test_file = "hw2_testing_data.txt"

test_data = read_data(test_file)

Eout = testing(test_data , record[dim][2] , record[dim][3] , len(test_data) , dim)

print 'Eout:' , Eout






 
