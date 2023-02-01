#https://itstory1592.tistory.com/35
import sys
input = sys.stdin.readline

#테스트 케이스
T = int(input())

for _ in range(T):
#출발점, 도착점 좌표
    x1, y1, x2, y2 = list(map(int, input().split()))
#행성계의 개수 n개
    n = int(input())
#행성계의 중점과 반지름(n개)
    count = 0
    #행성계 개수 반복하면서
    for i in range(n):
        #행성계의 중점과 반지름
        cx, cy, r = map(int, input().split())
        
        #거리 공식
        #행성의 중심 좌표와 출발점, 도착점 사이의 거리 구하기
        a = (x1 - cx)**2 + (y1 - cy)**2
        b = (x2 - cx)**2 + (y2 - cy)**2
        
        r_2 = r*r

        if r_2 > a and r_2> b:
            pass
        elif r_2 > a:
            count +=1
        elif r_2 > b:
            count +=1
    
    print(count)