#https://zoosso.tistory.com/890

import sys
from itertools import permutations
n , m = map(int, sys.stdin.readline().split(" "))
stack = list(map(int , sys.stdin.readline().split(" ")))
stack.sort()
ans = list(permutations(stack, m))
if m == 1:
    for t in range(0, len(ans)):
        s = list(ans[t])
        print(s[0])
else:
    for t in range(0,len(ans)):
        s = list(ans[t])
        for u in range(0,len(s)-1):
            print(s[u],end=" ")
        print(s[len(s)-1])