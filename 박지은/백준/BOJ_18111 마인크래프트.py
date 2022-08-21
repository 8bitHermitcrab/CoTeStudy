#마인크래프트
#https://blog.naver.com/hanjo1515/222500625112
##시간초과 해결 못했어요,,,,

import sys
input = sys.stdin.readline
N, M, B = map(int, input().split())

ddang = []
for i in range(N):
    ddang.append(list(map(int, input().split())))

# 최소층
# min_ddang1 = min(ddang)
# min_ddang2 = min(min_ddang1)

# 최대층
# max_ddang1 = max(ddang)
# max_ddang2 = max(max_ddang1)


#리스트는 시간을 많이 쓸 것 같다.....
#answer_timelist = []
#answer_floorlist=[]

min_time=999999999999
floor = 0

#최저층~최고층 사이에 땅 고르기 경우의 수
#for i in range(min_ddang2, max_ddang2+1):
###########이렇게 하니까 안됨#############


#256층 까지 땅을 i로 하는 경우의 수
for i in range(257):
    x_minus = 0
    x_plus = 0

    #이렇게 하면 오래 걸림(백준 질문 검색에서...)
    #for j in range(N):
    #    for k in range(M):

    for j in ddang:
        for k in j: 
         
            #층수보다 높은 경우 (블럭 뺄 때)
            if k >= i:
                x_minus += k - i
                
            #층수보다 낮은 경우(블럭 쌓을 때)
            elif k < i:
                x_plus += i - k
    
    #쌓을 블럭이 없는 경우
    if B + x_minus < x_plus:
        continue
    
    # 빼는건 *2, 채우는건 *1
    time = x_minus*2 + x_plus
    #최소 시간 비교하면서 업데이트 하기
    if time<=min_time:
        min_time = time
        floor = i

print(min_time, floor)
