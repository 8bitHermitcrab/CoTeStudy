# -*- coding: utf-8 -*-
"""주차요금계산

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uQjQYSkEdUCPFeqeUPdPsDXcMPPH6WUM
"""

def solution(fees, records):
    # fees=[기본시간, 기본요금, 단위시간, 단위요금]
    # records=["시각 차량번호 입/출차"]
    answer = []
    split_rec=''
    when_car_inout=[]
    # [시각,차량번호,입/출차]
    when=[]
    car=[]
    inout=[]
    for i in records:
        split_rec=i.split()
        when_car_inout.append(split_rec)
    for i in when_car_inout:
        when.append(i[0])
        car.append(i[1])
        inout.append(i[2])
    # [시각,시각,시각],[번호,번호,번호],[입출,입출,입출]
    for i in car:
        if car.count(i)%2==1:
            when.append('23:59')
            car.append(i)
            inout.append('OUT')
    # print(when,car,inout)
    for i in range(len(when)):
        when[i]=int(when[i][:2])*60+int(when[i][3:])
    car_inout={i:[] for i in car}
    for i in car_inout:
        for j in range(len(car)):
            if car[j]==i:
                car_inout[car[j]].append(j)
    # print(car_inout)
    # print(when,car)
    sum_lst=[]
    for i in car_inout.values():
        sum=0
        for j in range(len(i)):
            # [입차,출차,입차,출차]
            if j%2==0:
                when[i[j]]*=-1
            # [-입차,출차,-입차,출차]
        # print(when,i)
        for k in i:
            sum+=when[k]
        sum_lst.append(sum)
    # print(sum_lst)
    
    results={i:0 for i in car}
    for i in range(len(car_inout)):
        # print('\n',list(car_inout.keys()))
        results[list(car_inout.keys())[i]]=sum_lst[i]
    # print(sorted(results))
    
    for i in sorted(results):
        # print(results[i])
        if results[i]-fees[0]<0:
            answer.append(fees[1])
        elif (results[i]-fees[0])%fees[2]>0:
            answer.append(fees[1]+((results[i]-fees[0])//fees[2]+1)*fees[3])
        else:
            answer.append(fees[1]+((results[i]-fees[0])//fees[2]*fees[3]))
    print(5000+((334-180)//10+1)*600)
    return answer