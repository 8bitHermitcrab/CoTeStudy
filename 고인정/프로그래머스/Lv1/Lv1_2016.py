# 2016년

a = 5
b = 24

days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 지난 일
last_days = b-1

# 지난 달
for i in range(a-1):
    last_days += months[i]

last_days = last_days % 7
# print(last_days)

answer = days[last_days]
print(answer)

# https://jokerldg.github.io/algorithm/2021/04/03/2016.html
# https://jeongchul.tistory.com/641


'''
from datetime import datetime, date
def solution(a, b):
    today=['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer=today[date(2016,a,b).weekday()]
    return answer
'''