import numpy as np
import math
ms = 32
mh = 1
mu = ms*mh/(ms+mh)
alpha = 1.6627 #/AA-1
De = 3366.6578
#De = 28700
we = alpha*(math.sqrt(2*De/mu))
wx = (alpha**2)/(2*mu)
f = -987.05 #cm-1
beta = 92.11
g = math.cos(beta)/ms
def H(n1,n2,we,wx,mu,g,f,a):
    if n1 == n2:
        # print('here')
        a = we*(n1 + 0.5)
        b = wx*((n1 + 0.5)**2)
        c = we*(n2 + 0.5)
        d = wx*((n2 + 0.5)**2)
        # print(a,b,c,d)
        return ( a - b  + c - d )
    else:
        # print('not')
        if a > 0:
            a = (g*mu*we*0.5 + f*mu*wx*0.5)*(math.sqrt(n1+1))*(math.sqrt(n2+1))
            
            return (a)
        elif a < 0:
            b = (g*mu*we*0.5 + f*mu*wx*0.5)*math.sqrt(n1)*math.sqrt(n2)
            # c = -(g*mu*we*0.5 - f*mu*wx*0.5)*math.sqrt(n2)*(math.sqrt(n1+1)) 
            # d = -(g*mu*we*0.5 - f*mu*wx*0.5)*math.sqrt(n1)*(math.sqrt(n2+1)) 
            # b = (g*mu*we*0.5 + f*mu*wx*0.5)*math.sqrt(n1*n2)
            return (b)
        
a = 0.0
b = 0.0
for i in range (0,7):
    n1 = i
    for j in range (0,4):
        n2 = j
        a = a + H(n1,n2,we,wx,mu,g,f,1)
        b = b + H(n1,n2,we,wx,mu,g,f,-1)
        print(i, j, '+', a)
        print(i, j, '-', b)
        
