# -*- coding: utf-8 -*-
"""로또의 최고 순위와 최저 순위.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uQjQYSkEdUCPFeqeUPdPsDXcMPPH6WUM
"""

def solution(lottos, win_nums):
    worst=7
    for i in lottos:
        if i in win_nums:
            worst-=1
    best=worst-lottos.count(0)
    if worst==7:
        worst=6
    if best==7:
        best=6
    return [best,worst]