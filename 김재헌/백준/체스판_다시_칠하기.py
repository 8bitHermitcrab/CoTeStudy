# -*- coding: utf-8 -*-
"""체스판 다시 칠하기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uQjQYSkEdUCPFeqeUPdPsDXcMPPH6WUM
"""

N,M=map(int,input().split())
wboard=[0,1]*4
cnt=[]
for _ in range(N):
  horizontal=[0]*M
  a=input()
  for i in range(len(a)):
    if a[i]=='B':
      horizontal[i]=1      
  for i in range(M-7):
    sum_white=0
    for j in range(8):
      sum_white+=abs(horizontal[i:i+8][j]-wboard[j])
    cnt.append(sum_white)
best=32
for i in range(M-7):
  for j in range(N-7):
    white=sum(cnt[i::M-7][j:j+8][::2])+(32-sum(cnt[i::M-7][j:j+8][1::2]))
    if min(white,64-white)<best:
      best=min(white,64-white)
print(best)