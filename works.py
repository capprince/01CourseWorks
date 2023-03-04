# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 15:41:09 2022

@author: capprinceness
"""

##土力学分层总和计算
import numpy as np
a = np.array([0.8,1.6,2.4,3.2,4.0])
n1,n2 = 3, 1
b = (a*n1*(1+n1**2+2*a**2))/((1+n1**2+a**2)**0.5*(a**2+n1**2)*(a**2+1))+np.arctan(n1/(a*(1+n1**2+a**2)**0.5))
c = (a*n2*(1+n2**2+2*a**2))/((1+n2**2+a**2)**0.5*(a**2+n2**2)*(a**2+1))+np.arctan(n2/(a*(1+n2**2+a**2)**0.5))
d = 120/np.pi*(b-c)
e = []
for i in range(4):
    e.append((d[i]+d[i+1])/2)
e.append(2.362)
e = np.array(e)
s = e*0.8/2.5
print(s)


###道路与铁道工程作业，确定圆曲线半径
for i in range(50):
    R = 250+i*5 ##以5为步进确定圆半径
    L = 0.036*80**3/R
    if L < 66.67:
        L = 70###当L小于66.67时，取L = 70
    else:
        L = 5+5*(L/5)##L以5m取整
    if L < R/9:
        print('error:',R)##对计算出L小于R/9的R报错

print(7766/5)
