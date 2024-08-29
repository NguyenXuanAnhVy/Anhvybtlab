# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:28:03 2024

@author: Student
"""
import math
a = int(input("Nhap gio thu nhat: "))
b = int(input("Nhap phut thu nhat: "))
c = int(input("Nhap giay thu nhat: "))
d = int(input("Nhap gio thu hai: "))
e = int(input("Nhap phut thu hai: "))
f = int(input("Nhap giay thu hai: "))
x = int(input("Nhap 1 de cong, nhap 2 de tru: "))
V = a*3600 + b*60 + c
D = d*3600 + e*60 + f
if x == 1:
    print("Ket qua phep cong: ", V+D)
elif x == 2:
    print("Ket qua phep tru: ", V-D)
else:
    print("Loi")