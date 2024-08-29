# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:26:18 2024

@author: Student
"""

import math
gio= int(input("Nhap gio: "))
phut= int(input("Nhap phut: "))
giay= int(input("Nhap giay: "))
hps= "{}h:{}p:{}s". format(gio, phut, giay)
print(hps)
tonggiay= gio*3600 + phut*60 + giay
print("Tong giay la: ", tonggiay)