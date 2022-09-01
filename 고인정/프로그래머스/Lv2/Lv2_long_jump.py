# 멀리 뛰기

n = 4

def solution(n):
    table = dict()
    # 0칸 = 1가지
    # 1칸 = 1가지
    # 2칸 = 2가지(1칸 뛰는 경우 + 2칸 뛰는 경우)
    # 3칸 = 3가지(1칸 뛰는 경우 + 2칸 뛰는 경우)
    table[0], table[1] = 1, 1

    print(f'=== table = {table} ===')

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
        print(f'table[{i}] = {table[i]}')
        print(f'table[{i}] = table[{i-1}] + table[{i-2}] ::: {table[i]} = {table[i-1]} + {table[i-2]}')

    return table[n] % 1234567

print(solution(n))

# https://inspirit941.tistory.com/148


'''
def solution(n):
    cnt = 1
    
    min_max = [1, 2]

    stack = []
    # num = 4, 3, 2, 1
    num = 4
    way = [] 
    way1 = [1] * n
    print(way1)
    max = 2
    min = 1
    while num != 0:
        stack.append(max)
        num = num - max
        stack.append(min)
        num = num - min
        print(stack)
        

    answer = cnt % 1234567
    return answer

print(solution(n))
'''