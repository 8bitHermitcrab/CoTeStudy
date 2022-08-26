####78%에서 자꾸 틀림..


import sys
input = sys.stdin.readline

M = int(input())

#집합
S=set()


for _ in range(M):
    x = list(input().rstrip().split())
    #add
    if x[0] == 'add':
        S.add(x[1])
    #remove
    if x[0] == 'remove':
        S.discard(x[1])
    #check
    if x[0] == 'check':
        if x[1] in S:
            print(1)
        else:
            print(0)
    #toggle
    if x[0] == 'toggle':
        if x[1] in S:
            S.remove(x[1])
        else:
            S.add(x[1])
    #all
    if x[0] == 'all':
        S = set([range(1, 21)])
    #empty
    if x[0] == 'empty':
        S.clear()
