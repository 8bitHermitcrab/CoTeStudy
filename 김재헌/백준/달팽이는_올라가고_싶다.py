# -*- coding: utf-8 -*-
"""달팽이는 올라가고 싶다.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uQjQYSkEdUCPFeqeUPdPsDXcMPPH6WUM
"""

a,b,v=map(int,input().split())

if a>=v:
  print(1)
elif (v-a)%(a-b)==0:
    print((v-a)//(a-b)+1)
else:
    print((v-a)//(a-b)+2)