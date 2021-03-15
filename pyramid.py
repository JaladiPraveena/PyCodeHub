# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 10:45:31 2021

@author: DELL
"""


for i in range(-5,6):
    print(abs(i)*' '+'*'*abs(abs(i)-6)+'*'*abs(abs(i)-5))
    



h = 12; w = 0
while h > 0 and w < 33 :
    print(' '*h+'/_\\'+'/_\\'*w)
    h -= 1
    w += 1

p="*"
for i in range(6):
    if i <=3:
        print(*p*i, sep='')
    else:
        print(p*(i+1))