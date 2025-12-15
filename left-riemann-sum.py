import math

def f(x):
  return math.exp(x)

def leftriemann(f,a,b,n):
  area = 0
  delta_x = (b-a)/n
  for i in range(n+1):
    area += f(a+i*delta_x)*delta_x
  
