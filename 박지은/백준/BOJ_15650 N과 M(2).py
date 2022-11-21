N, M = map(int, input().split())

#1번 풀이

nums_lst = [ _ for _ in range(1, N+1)]

#print(nums_lst)
#3C1 = 3
#4C2 = 6
#4C4 = 1
#combination...

from itertools import combinations

combi = list(combinations(nums_lst, M))

#print(combi)

for i in combi:
    i = str(i)
    #print(len(i))
    if len(i) == 4:
        print(int(i[1]))
    #print(i)
    else:
        temp = []
        for j in i:
            if j == "(" or j == ")" or j == "," or j == " ":
                continue
            else:
                temp.append(int(j))
        print(*temp)

#2번 풀이
#https://blog.naver.com/kimsamuel351/222690463776
from itertools import combinations
N, M = map(int, input().split())
nums = combinations(range(1, N+1), M)

for i in nums:
    print(' '.join(map(str, i)))