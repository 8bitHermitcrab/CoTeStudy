# 하노이의 탑

# 2개 [ [1,2], [1,3], [2,3] ]
# 3개 [ [1 : 1,2], [2: 1,3], [1: 2, 3], [] ]


# tower1     tower2       tower3
# 1탑         2탑           3탑
# 3 2 1       
# 3 2         1     
# 3            1           2
# 3                        2 1
#              3           2 1
#             3 1           2
# 2           3 1              
# 2 1          3                
# 2 1                       3
# 2            1            3
#              1            3 2
#                           3 2 1

n = 2

# tower1 = [i for i in range(n, 0, -1)]
# tower2 = []
# tower3 = []
# answer = []
'''
while len(tower3) != n:
    # len(tower1) == n and len(tower2) == 0
    if len(tower1) == n and len(tower2) == 0:
        tower2.append(tower1.pop())
        answer.append([1, 2])
    # len(tower1) == n-1 and len(tower3) == 0
    elif len(tower1) == n-1 and len(tower3) == 0:
        tower3.append(tower1.pop())
        answer.append([1, 3])
    elif '''

def hanoi(n, start, end, mid, answer):
    if n == 1:
        # print([1, 3])
        return answer.append([start, end])
    else:
        # 1번 기둥에 있는 n개의 원반 중 n-1개를 2번 기둥으로 옮긴다. (3번 기둥을 거쳐감)
        hanoi(n-1, start, mid, end, answer)
        # print([start, end])
        answer.append([start, end])
        # 2번 기둥에 있는 n-1개의 원반을 다시 3번 기둥으로 옮긴다. (1번 기둥을 거쳐감)
        hanoi(n-1, mid, end, start, answer)

def solution(n):
    answer = []
    # start = 1
    # mid = 2
    # end = 3
    
    hanoi(n, 1, 3, 2, answer)
    return answer


print(solution(n))

# https://shoark7.github.io/programming/algorithm/tower-of-hanoi
# https://m.blog.naver.com/jaeyoon_95/221762231876
# https://www.youtube.com/watch?v=FYCGV6F1NuY
