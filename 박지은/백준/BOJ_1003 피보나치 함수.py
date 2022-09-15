#220915 피보나치 함수
#https://bio-info.tistory.com/122

#  [zero, one]
#fibonacci(0) = [1, 0]
#fibonacci(1) = [0, 1]
#fibonacci(2) = fibonacci(1), fibonacci(0) = [1, 1]
#fibonacci(3) = fibonacci(2), fibonacci(1) = [1, 2]
#fibonacci(4) = fibonacci(3), fibonacci(2) = [2, 3]
#fibonacci(5) = fibonacci(4), fibonacci(3) = [3, 5]
#fibonacci(6) = fibonacci(5), fibonacci(4) = [5, 8]


#0이 출력되는 규칙: 1, 0, 1, 1, 2, 3
#1이 출력되는 규칙: 0, 1, 1, 2, 3
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x = int(input())
    zero, one = 1, 0
    for i in range(x):
        zero, one = one, zero+one
    print(zero, one)



