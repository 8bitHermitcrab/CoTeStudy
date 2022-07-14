# 서울에서 김서방 찾기

seoul = ["Jane", "Kim"]

answer = ''

for i in range(len(seoul)):
    kim = 'Kim'
    if seoul[i] == kim:
        answer = '김서방은 ' + str(i) + '에 있다'
    
print(answer)