# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:09:07 2024

@author: Student
"""

import math
n= int(input("Nhap so nguyen: "))
chuoi= ["Khong doc duoc", "Mot", "Hai", "Ba", "Bon", "Nam", "Sau", "Bay", "Tam", "Chin"]
if 0 < n <= 9:
    print(chuoi[n])
else:
    print(chuoi[0])