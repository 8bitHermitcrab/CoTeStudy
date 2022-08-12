# 프린터 큐

from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0

    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1

        if best == front:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        
        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1

# https://hongcoding.tistory.com/42

# 3           -> 3번 테스트 할 것
# 1 0         -> n = 1, m = 0
# 5           -> 중요도 = 5
# 4 2         -> n = 4, m = 2
# 1 2 3 4     -> 중요도 = 1 2 3 4
# 6 0         -> n = 6, m = 0
# 1 1 9 1 1 1 -> 중요도 = 1 1 9 1 1 1

# 9 1 1 1 1 1
'''
# 테스트 케이스
t =  int(input())

# n, m번째
for _ in range(t):
    # 문서의 개수 n, 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M
    n, m = list(map(int, input().split()))
    # 중요도
    p = list(map(int, input().split()))
    idx = [i for i in range(len(p))]
    idx[m] = 'target'

    # print(f'n = {n}, m = {m}')
    # print(f'p = {p}')
    # print(f'idx = {idx}')


    # 순서
    order = 0

    for i in p:
        if i == max(p):
            order += 1

            if idx[0] == 'target':
                print(order)
                break
            else:
                p.pop(0)
                idx.pop(0)

        else:
            p.append(p.pop(0))
            idx.append(idx.pop(0))


# https://assaeunji.github.io/python/2020-05-04-bj1966/
'''