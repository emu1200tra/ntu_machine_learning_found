from numpy import *
from matplotlib import pyplot as plt

with open('hw1_data.txt') as file:
  lines = [line.split() for line in file]

for line in lines:
  line.append(line[-1])
  line[-2] = 1

lines = array(lines)
lines = lines.astype(float)
weight = [0 , 0 , 0 , 0 , 0]
times = 1
update_freq = [0]*256
total_count = 0
max_num = 0
for i in range(2000):
  while True:
    flag = 1
    for line in lines:
      t = dot(weight , line[0:-1])
      if t == 0.0:
        a = sign(-1.0)
      else:
        a = sign(t)
      if a != sign(line[-1]):
        times += 1
        
        flag = 0
        weight += line[-1] * line[0:-1]
    if flag:
      break
  update_freq[times] += 1
  random.shuffle(lines[:])
  weight = [0 , 0 , 0 , 0 , 0]
  if max_num < times:
    max_num = times
  total_count += times
  times = 0

print total_count/2000

plt.bar(range(0 , max_num+1) , update_freq[0:max_num+1])
outputstring = 'update times (with average: ' + str(total_count/2000) + ')'
plt.xlabel(outputstring)
plt.ylabel('frequency')
plt.show()