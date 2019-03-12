from math import cos, sin


for e in range(10, 30):
    h = 10**(-e)
    print("h = {}, (f(1+h)-f(1))/h = {}, denom = {}".format(h, (cos(1+h)-cos(1))/h, cos(1+h)-cos(1)))

for e in range(10, 30):
    h = 10**(-e)
    print("h = {}, -2sin(1+h/2)sin(h/2)/h = {}".format(h, -2*sin(1+h/2)*sin(h/2)/h))
    
    
    
