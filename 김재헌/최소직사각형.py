# -*- coding: utf-8 -*-
"""최소직사각형

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KdAmXJto7SHorOtiXExR4tzlzlXqbQuC
"""

def solution(sizes):
    maxs=[]
    mins=[]
    for i in sizes:
        maxs.append(max(i))
        mins.append(min(i))
    answer=max(maxs)*max(mins)
    return answer