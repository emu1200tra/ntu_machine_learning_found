from math import exp
'''
def gradient(x , y):
  #x
  resultx = -3.0 + exp(x) + 2.0*x - 2.0*y + exp((x*y))*y
  #y
  resulty = -2.0 + 2.0*exp(2*y) - 2.0*x + exp(x*y)*x + 4.0*y

  return resultx , resulty

def E(u , v):
  result = exp(u)+exp(2.0*v)+exp(u*v)+u**2.0 - 2.0*u*v + 2.0*v**2.0 - 3.0*u - 2.0*v
  return result


point = (0.0 , 0.0)
for i in range(6):
  gradientresult = gradient(point[0] , point[1])
  #print gradientresult
  point = (point[0] - 0.01*gradientresult[0] , point[1] - 0.01*gradientresult[1])
  print point
print E(point[0] , point[1])

print "1 , 1:" , E(0.02 , 0.0)
'''
'''
def gradient(x , y):
  #x
  resultx = -(-3.0 + exp(x) + 2.0*x - 2.0*y + exp((x*y))*y)/(2.0 + exp(x) + exp(x*y)*(y**2))
  #y
  resulty = -(-2.0 + 2.0*exp(2.0*y) - 2.0*x + exp(x*y)*x + 4.0*y)/(4.0 + 4.0*exp(2.0*y) + exp(x*y)*(x**2))

  return resultx , resulty

def E(u , v):
  result = exp(u)+exp(2.0*v)+exp(u*v)+u**2.0 - 2.0*u*v + 2.0*v**2.0 - 3.0*u - 2.0*v
  return result


point = (0.0 , 0.0)
for i in range(6):
  gradientresult = gradient(point[0] , point[1])
  #print gradientresult
  point = (point[0] + gradientresult[0] , point[1] + gradientresult[1])
  print point
print E(point[0] , point[1])
'''
#print "1 , 1:" , E(0.02 , 0.0)
