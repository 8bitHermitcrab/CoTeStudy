# 코드 출처
# https://hwisaek.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-N%EA%B0%9C%EC%9D%98-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98-Python

# A와 B의 최소공배수 = A * B / A와 B의 최대공약수
# -> https://jwj4519.com/entry/%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%99%80-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98%EC%9D%98-%EA%B4%80%EA%B3%84-%EC%A4%91%EB%93%B1%EC%88%98%ED%95%99

# gcd(x.y) : x와 y의 최대공약수
# math.gcd(answer, n)

import math
 
def solution(arr):
    answer = 1
    # arr에서 1개씩 추가해서 N개의 최소공배수 구하기
    for n in arr:
        answer = n * answer // math.gcd(answer, n)
    return answer

# def solution(arr):
#     #최소공배수 -> 약수들 구해서 곱하기
#     #약수 구하기
#     #이 방법으로는 모르겠다... -> 검색....
#     for i in range(len(arr)):
#         n = i
#         temp_lst = []
#         for j in range(1, i+1):
#             if arr[i-1] % i == 0:
#                 temp_lst.append(j)
#                 n = int(n/i)
            
#     answer = 0
#     return answer