import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
ms = 32
mh = 1
mu = ms*mh/(ms+mh)
n1 = [0,1,2,1,3,2,4,3,5,4,6,5,4,3,6,7]
n2 = [0,0,0,1,0,1,0,1,0,1,0,1,2,3,0,0]
# data = {n1 :[0,1,2,1,3,2,4,3,5,4,6,5,4,3,6,7],
# n2 :[0,0,0,1,0,1,0,1,0,1,0,1,2,3,0,0]}
# x = 
E = [0.0,2614.4079,5144.9862,5243.1014,7576.3833,7752.2638,9911.0230,10188.301,12149.458,12524.628,14291.122,16334.162]

def H(n1,n2,we,alpha,mu,g,f,a):
    if n1 == n2:
        # print('here')
        a = we*(n1 + 0.5)
        b = (2*mu*alpha**2)*((n1 + 0.5)**2)
        c = we*(n2 + 0.5)
        d = (2*mu*alpha**2)*((n2 + 0.5)**2)
        # print(a,b,c,d)
        return ( a - b  + c - d )
    else:
        # print('not')
        if a > 0:
            a = (g*mu*we*0.5 + f*mu*(2*mu*alpha**2)*0.5)*(math.sqrt(n1+1))*(math.sqrt(n2+1))
            
            return (a)
        elif a < 0:
            b = (g*mu*we*0.5 + f*mu*(2*mu*alpha**2)*0.5)*math.sqrt(n1)*math.sqrt(n2)
            # c = -(g*mu*we*0.5 - f*mu*wx*0.5)*math.sqrt(n2)*(math.sqrt(n1+1)) 
            # d = -(g*mu*we*0.5 - f*mu*wx*0.5)*math.sqrt(n1)*(math.sqrt(n2+1)) 
            # b = (g*mu*we*0.5 + f*mu*wx*0.5)*math.sqrt(n1*n2)
            return (b)

# for i in range(0,len(n1),1):
g, f, alpha, we = optimize.curve_fit(H, n1,n2, E)
print(g,f,alpha,we)

# def H1{}:
#     a = (g*mu*we*0.5 + f*mu*wx*0.5)*(math.sqrt(n1+1))*(math.sqrt(n2+1))
#     b = (g*mu*we*0.5 + f*mu*wx*0.5)*math.sqrt(n1)*math.sqrt(n2)
#     c = -(g*mu*we*0.5 - f*mu*wx*0.5)*math.sqrt(n2)*(math.sqrt(n1+1)) 
#     d = -(g*mu*we*0.5 - f*mu*wx*0.5)*math.sqrt(n1)*(math.sqrt(n2+1)) 