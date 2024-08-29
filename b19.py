# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:28:09 2024

@author: Student
"""
import math
a= int(input("Nhap gia tri a: "))
b= int(input("Nhap gia tri b: "))
c= int(input("Nhap gia tri c: "))
d= int(input("Nhap gia tri d: "))
if a<=b and a<=c and a<=d:
    print("Gia tri nho nhat: ", a)
elif b<=a and b<=c and b<=d:
    print("Gia tri nho nhat: ", b)
elif c<=a and c<=b and c<=d: 
    print("Gia tri nho nhat: ", c)
else:
    print("Gia tri nho nhat: ", d)
