# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:21:22 2024

@author: Student
"""

gio = int(input("Nhap gio:"))
phut = int(input("Nhap phut:"))
giay = int(input("Nhap giay:"))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print("Gio, phut, giay hop le.")
else:
    print("Gio, phut, giay khong hop le.")