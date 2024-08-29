# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:28:44 2024

@author: Student
"""

ky_tu = input("Nhap mot ky tu: ")
if ky_tu.islower():
  ky_tu_moi = ky_tu.upper()
else:
    ky_tu_moi = ky_tu.lower()
print("Ky tu sau khi chuyen doi:", ky_tu_moi)