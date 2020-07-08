# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 00:29:06 2020

@author: USER
"""

import numpy as np
import pandas as pd

import tkinter
from tkinter import messagebox

   
def showMsg():
   result = ''
   for i in check_v:
       if check_v[i].get() == True:
            result = result + variables[i]+' '
            
   Ans=messagebox.askquestion('房屋每坪價格與變數之間的關係','您想了解的變數是：'+result)
   if(Ans=='yes'):
         win.destroy()
         

win=tkinter.Tk()
win.title('房屋每坪價格與變數之間的關係')
win.geometry('400x300')   #視窗格式

label=tkinter.Label(win, text='請選取您想了解的變數：').pack()

variables = {0:'成交日期', 1:'屋齡', 2:'離最近捷運站的距離', 3:'周圍便利商店數量',4:'經度',5:'緯度'}
check_v ={}
for i in range(len(variables)):
    check_v[i] = tkinter.BooleanVar()
    tkinter.Checkbutton(win, text=variables[i], variable=check_v[i]).pack()  #主視窗

tkinter.Button(win, text='確定', command=showMsg).pack()

win.mainloop()


data = pd.read_csv('datasets_88705_204267_Real estate.csv',header=0,index_col=0)
real_state = np.array(data)

house_price_of_unit_area = real_state[:,6]
longitude = real_state[:,5]
latitude = real_state[:,4]
number_of_convenience_stores = real_state[:,3]
distance_to_the_nearest_MRT_station = real_state[:,2]
house_age = real_state[:,1]
transaction_date = real_state[:,0]


sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0
sum_5 = 0
sum_6 = 0
sum_7 = 0

print('='*80)

for i in range(len(transaction_date)):
    sum_1 = sum_1 + transaction_date[i]
    avg_1 = sum_1/len(transaction_date)

print(f'本資料成交日期的平均為:{round(avg_1,4)}')

for i in range(len(house_age)):
    sum_2 = sum_2 + house_age[i]
    avg_2 = sum_2/len(house_age)

print(f'本資料屋齡的平均為:{round(avg_2,4)}年')

for i in range(len(distance_to_the_nearest_MRT_station)):
    sum_3 = sum_3 + distance_to_the_nearest_MRT_station[i]
    avg_3 = sum_3/len(distance_to_the_nearest_MRT_station)

print(f'本資料離最近捷運站的距離的平均為:{round(avg_3,4)}公尺')

for i in range(len(number_of_convenience_stores)):
    sum_4 = sum_4 + number_of_convenience_stores[i]
    avg_4 = sum_4/len(number_of_convenience_stores)

print(f'本資料周圍便利商店數量的平均為:{round(avg_4,4)}家')

for i in range(len(latitude)):
    sum_5 = sum_5 + latitude[i]
    avg_5 = sum_5/len(latitude)

print(f'本資料經度的平均為:{round(avg_5,4)}')

for i in range(len(longitude)):
    sum_6 = sum_6 + longitude[i]
    avg_6 = sum_6/len(longitude)

print(f'本資料緯度的平均為:{round(avg_6,4)}')

for i in range(len(house_price_of_unit_area)):
    sum_7 = sum_7 + house_price_of_unit_area[i]
    avg_7 = sum_7/len(house_price_of_unit_area)

print(f'本資料每坪價格的平均為:{round(avg_7,4)}萬')

print('='*80)
one_col = np.ones((414,1))
array_1 = one_col

for i in range(6):
    if check_v[i].get() == True:
        array_1 = np.c_[array_1,real_state[:,i]]    

array_2 = house_price_of_unit_area.reshape(414,1)

equation = np.linalg.lstsq(array_1,array_2,rcond=None)

x1 = 0
x2 = 0
x3 = 0
x4 = 0
x5 = 0
x6 = 0

if len(equation[0])==2:
    Y = equation[0][0][0]+equation[0][1][0]*x1
    for i in range(len(equation[0])) :
        if equation[0][i][0] < 0 :
            a = ''
        else:
            a = '+'
    print(f'根據您所選的變數得出來的方程式為:Y = {round(equation[0][0][0],4)}{a}{round(equation[0][1][0],4)}*x1')
    
if len(equation[0])==3:
    Y = equation[0][0][0]+equation[0][1][0]*x1+equation[0][2][0]*x2
    if equation[0][1][0] < 0 :
        a = ''
    else:
        a = '+'
        
    if equation[0][2][0] < 0 :   
        b = ''
    else:
        b = '+'
        
    print(f'根據您所選的變數得出來的方程式為:Y = {round(equation[0][0][0],4)}{a}{round(equation[0][1][0],4)}*x1{b}{round(equation[0][2][0],4)}*x2')
        
if len(equation[0])==4:
    Y = equation[0][0][0]+equation[0][1][0]*x1+equation[0][2][0]*x2+equation[0][3][0]*x3
    if equation[0][1][0] < 0 :
        a = ''
    else:
        a = '+'
        
    if equation[0][2][0] < 0 :   
        b = ''
    else:
        b = '+'
        
    if equation[0][3][0] < 0 :
        c = ''
    else:
        c = '+'
        
    print(f'根據您所選的變數得出來的方程式為:Y = {round(equation[0][0][0],4)}{a}{round(equation[0][1][0],4)}*x1{b}{round(equation[0][2][0],4)}*x2{c}{round(equation[0][3][0],4)}*x3')

if len(equation[0])==5:
    Y = equation[0][0][0]+equation[0][1][0]*x1+equation[0][2][0]*x2+equation[0][3][0]*x3+equation[0][4][0]*x4
    if equation[0][1][0] < 0 :
        a = ''
    else:
        a = '+'
        
    if equation[0][2][0] < 0 :   
        b = ''
    else:
        b = '+'
        
    if equation[0][3][0] < 0 :
        c = ''
    else:
        c = '+'
        
    if equation[0][4][0] < 0 :
        d = ''
    else:
        d = '+'
    print(f'根據您所選的變數得出來的方程式為:Y = {round(equation[0][0][0],4)}{a}{round(equation[0][1][0],4)}*x1{b}{round(equation[0][2][0],4)}*x2{c}{round(equation[0][3][0],4)}*x3{d}{round(equation[0][4][0],4)}*x4')

if len(equation[0])==6:
    Y = equation[0][0][0]+equation[0][1][0]*x1+equation[0][2][0]*x2+equation[0][3][0]*x3+equation[0][4][0]*x4+equation[0][5][0]*x5
    if equation[0][1][0] < 0 :
        a = ''
    else:
        a = '+'
        
    if equation[0][2][0] < 0 :   
        b = ''
    else:
        b = '+'
        
    if equation[0][3][0] < 0 :
        c = ''
    else:
        c = '+'
        
    if equation[0][4][0] < 0 :
        d = ''
    else:
        d = '+'
    
    if equation[0][5][0] < 0 :
        e = ''
    else:
        e = '+'
    print(f'根據您所選的變數得出來的方程式為:Y = {round(equation[0][0][0],4)}{a}{round(equation[0][1][0],4)}*x1{b}{round(equation[0][2][0],4)}*x2{c}{round(equation[0][3][0],4)}*x3{d}{round(equation[0][4][0],4)}*x4{e}{round(equation[0][5][0],4)}*x5')
    
if len(equation[0])==7:    
    Y = equation[0][0][0]+equation[0][1][0]*x1+equation[0][2][0]*x2+equation[0][3][0]*x3+equation[0][4][0]*x4+equation[0][5][0]*x5+equation[0][6][0]*x6
    
    if equation[0][1][0] < 0 :
        a = ''
    else:
        a = '+'
        
    if equation[0][2][0] < 0 :   
        b = ''
    else:
        b = '+'
        
    if equation[0][3][0] < 0 :
        c = ''
    else:
        c = '+'
        
    if equation[0][4][0] < 0 :
        d = ''
    else:
        d = '+'
    
    if equation[0][5][0] < 0 :
        e = ''
    else:
        e = '+'
        
    if equation[0][6][0] < 0 :
        f = ''
    else:
        f = '+'    
    print(f'根據您所選的變數得出來的方程式為:Y = {round(equation[0][0][0],4)}{a}{round(equation[0][1][0],4)}*x1{b}{round(equation[0][2][0],4)}*x2{c}{round(equation[0][3][0],4)}*x3{d}{round(equation[0][4][0],4)}*x4{e}{round(equation[0][5][0],4)}*x5{f}{round(equation[0][6][0],4)}*x6')

print('='*80)

print(f'基礎房價為每坪{round(equation[0][0][0],4)}萬元')

for i in range(6):
    if check_v[i].get() == True:
        print(f'每增加一單位{variables[i]}:')
        
        
for i in range(len(equation[0])):
    if i == 0 :
        continue
    else:
        print(f'便會增加{round(equation[0][i][0],4)}萬元的每坪房價')
    
print('='*80)        

def check_float(num):
    result = 0
    try:
        float(num)
    except ValueError :   
        result = False                  
    else:
        result = True                  
    finally:
        return result 
        
if len(equation[0])==2:
    while True:
       x1=float(input('輸入第一個變數的值為:'))
       if (not check_float(x1)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    Y = equation[0][0][0]+equation[0][1][0]*x1

if len(equation[0])==3:
    while True:
       x1=float(input('輸入第一個變數的值為:'))
       if (not check_float(x1)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    while True:
       x2=float(input('輸入第二個變數的值為:'))
       if (not check_float(x2)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    Y = equation[0][0][0]+equation[0][1][0]*x1+equation[0][2][0]*x2
    
if len(equation[0])==4: 
    while True:
       x1=float(input('輸入第一個變數的值為:'))
       if (not check_float(x1)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    while True:
       x2=float(input('輸入第二個變數的值為:'))
       if (not check_float(x2)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    while True:
       x3=float(input('輸入第三個變數的值為:'))
       if (not check_float(x3)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    Y = equation[0][0][0]+equation[0][1][0]*x1+equation[0][2][0]*x2+equation[0][3][0]*x3

if len(equation[0])==5: 
    while True:
       x1=float(input('輸入第一個變數的值為:'))
       if (not check_float(x1)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    while True:
       x2=float(input('輸入第二個變數的值為:'))
       if (not check_float(x2)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    while True:
       x3=float(input('輸入第三個變數的值為:'))
       if (not check_float(x3)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    while True:
       x4=float(input('輸入第四個變數的值為:'))
       if (not check_float(x4)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    Y = equation[0][0][0]+equation[0][1][0]*x1+equation[0][2][0]*x2+equation[0][3][0]*x3+equation[0][4][0]*x4

if len(equation[0])==6: 
    while True:
       x1=float(input('輸入第一個變數的值為:'))
       if (not check_float(x1)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    while True:
       x2=float(input('輸入第二個變數的值為:'))
       if (not check_float(x2)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    while True:
       x3=float(input('輸入第三個變數的值為:'))
       if (not check_float(x3)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    while True:
       x4=float(input('輸入第四個變數的值為:'))
       if (not check_float(x4)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break
    while True:
       x5=float(input('輸入第五個變數的值為:'))
       if (not check_float(x5)):
          print('輸入變數有錯誤，請重新', end='')
          continue
       else:
          break

if len(equation[0])==7:        
    while True:
     x1=float(float(input('輸入第一個變數的值為:')))
     if (not check_float(x1)):
        print('輸入變數有錯誤，請重新', end='')
        continue
     else:
        break
    while True:
     x2=float(input('輸入第二個變數的值為:'))
     if (not check_float(x2)):
        print('輸入變數有錯誤，請重新', end='')
        continue
     else:
        break
    while True:
     x3=float(input('輸入第三個變數的值為:'))
     if (not check_float(x3)):
        print('輸入變數有錯誤，請重新', end='')
        continue
     else:
        break
    while True:
     x4=float(input('輸入第四個變數的值為:'))
     if (not check_float(x4)):
        print('輸入變數有錯誤，請重新', end='')
        continue
     else:
        break
    while True:
     x5=float(input('輸入第五個變數的值為:'))
     if (not check_float(x5)):
        print('輸入變數有錯誤，請重新', end='')
        continue
     else:
        break
    while True:
     x6=float(input('輸入第六個變數的值為:'))
     if (not check_float(x6)):
        print('輸入變數有錯誤，請重新', end='')
        continue
     else:
        break
    Y = equation[0][0][0]+equation[0][1][0]*x1+equation[0][2][0]*x2+equation[0][3][0]*x3+equation[0][4][0]*x4+equation[0][5][0]*x5+equation[0][6][0]*x6

print('='*80)

print(f'所得出來的預測房價為:{round(Y,4)} 萬元/坪')

