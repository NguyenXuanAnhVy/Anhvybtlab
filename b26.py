# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:29:00 2024

@author: Student
"""

import math
#26a
a= float(input("Nhap a: "))
b= float(input("Nhap b: "))
c= float(input("Nhap c: "))
if a>b:
    a, b = b, a
if a>c:
   #Doi cho a va c
   a, c = c, a
if b>c:
   #Doi cho b va c
   b, c = c, b
print("Nhap so thu tu tang dan cua ba so la: ", a, b, c)
#26b
a= int(input("Nhap so nguyen a: "))
b= int(input("Nhap so nguyen b: "))
c= int(input("Nhap so nguyen c: "))
d= int(input("Nhap so nguyen d:"))
if a>b:
    a, b = b, a
if a>c:
   #Doi cho a va c
   a, c = c, a
if a>d:
    a, d = d, a
if b>c:
   #Doi cho b va c
   b, c = c, b
if b>d:
    b, d = d, b
if c>d:
    c, d = d, c
print("Nhap so nguyen theo thu tu tang dan: ", a, b, c, d)
   