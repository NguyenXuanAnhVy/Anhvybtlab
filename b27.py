# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 22:16:18 2024

@author: anhvy 
"""
import math 
hinh= input("Chon hinh")
#Hinh vuong:
if hinh == 'v':
 v= input("Hinh vuong")  
 chieudai= float(input("Nhap chieu dai hinh vuong: "))
 chuvi_v= chieudai*4
 dientich_v= chieudai**2
 print("Chu vi hinh vuong= ", chuvi_v)
 print("Dien tich hinh vuong= ", dientich_v)
#Hinh chu nhat:
elif hinh == 'n':
 n= input("Hinh chu nhat")
 chieudai_n= float(input("Nhap chieu dai hinh chu nhat: "))
 chieurong_n= float(input("Nhap chieu rong hinh chu nhat: "))
 chuvi_n= (chieudai_n + chieurong_n)*2
 dientich_n= chieudai_n * chieurong_n 
 print("Chu vi hinh chu nhat= ", chuvi_n)
 print("Dien tich hinh chu nhat= ", dientich_n)
#Hinh tron:
elif hinh == 't':
 t= input("Hinh tron")
 bankinh= float(input("Ban kinh hinh tron: "))
 chuvi_t= 2*bankinh*3.14
 dientich_t= ((bankinh)**2)*3.14
 print("Chu vi hinh tron= ", chuvi_t)
 print("Dien tich hinh tron= ", dientich_t)
    