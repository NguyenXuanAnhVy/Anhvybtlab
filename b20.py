# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:28:30 2024

@author: Student
"""
import math
a= int(input("Nhap gia tri a: "))
b= int(input("Nhap gia tri b: "))
c= int(input("Nhap gia tri c: "))
if a>=b and a>=c:
    print("Gia tri lon nhat: ", a)
elif b>=a and b>=c:
    print("Gia tri lon nhat: ", b)
else:
    print("Gia tri lon nhat: ", c)