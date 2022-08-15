# 주차 요금 계산

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

# def getTime(time):
#     h, m = time.split(':')
#     return int(h) * 60 + int(m)

import math 

def total_fee(minutes, fees):
    return fees[1] + math.ceil(max(0, (minutes - fees[0])) / fees[2]) * fees[3]

def solution(fees, records):
    answer = []
    parking = dict()
    stack = dict()    
    
    for record in records:
        time, car_num, inout = record.split()
        h, m = time.split(':')
        minutes = int(h) * 60 + int(m)
        # time = getTime(time)
        if inout == 'IN':
            parking[car_num] = minutes
        elif inout == 'OUT':
            try:
                stack[car_num] += minutes - parking[car_num]
            except:
                stack[car_num] = minutes - parking[car_num]
            # 출차 차량 삭제
            del parking[car_num]
    
    # OUT 없을 때 23:59 처리
    for car_num, minute in parking.items():
        try:
            stack[car_num] += ((23 * 60) + 59) - minute
        except:
            stack[car_num] = ((23 * 60) + 59) - minute

    for car_num, time in sorted(list(stack.items())):
        # print(car_num, time)
        answer.append(total_fee(time, fees))

    return answer

print(solution(fees, records))


# https://kjhoon0330.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%B0%A8-%EC%9A%94%EA%B8%88-%EA%B3%84%EC%82%B0-Python


# https://latte-is-horse.tistory.com/326