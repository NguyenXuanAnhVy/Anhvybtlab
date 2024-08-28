# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:54:34 2024

@author: Student
"""
import math
a= input("Nhap gio, phut, giay:")
b= a.split(":")
hh, mm, ss= map(int,b)
tonggiay= hh*3600 + mm*60 + ss
print("Tong giay la: ", tonggiay)