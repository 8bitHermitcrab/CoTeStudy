# -*- coding: utf-8 -*-
"""이진 변환 반복하기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uQjQYSkEdUCPFeqeUPdPsDXcMPPH6WUM
"""

def solution(s):
    answer = []
    cnt=0
    ones=s.count('1') #3
    zeros=s.count('0') #2
    while s!='1': 
        #01110
        ones=s.count('1')#3
        print('ones:',ones)
        s=bin(int(ones))[2:]
        print('s:',s)   
        zeros+=s.count('0') #2
        print('zeros:',zeros)
        cnt+=1
        print(ones,zeros,s)
   # if s[-1]=='0':
      #  cnt+=1

    return [cnt,zeros]