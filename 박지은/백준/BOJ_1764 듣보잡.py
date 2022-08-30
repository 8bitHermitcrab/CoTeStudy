#6달전 코드 -> 딕셔너리로 풀기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

diname = {}
kk =[]

#듣x(d)
for i in range(n+m):
    name = input().rstrip()
    if name in diname:
        diname[name] =+ 1
    else:
        diname[name] = 0
#print(diname)

for key, val in diname.items():
    if val == 1:
        kk.append(key)

print(len(kk))
print(*sorted(kk), sep = '\n')


#set으로 풀기
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

A = set()
B = set()

for i in range(n):
    A.add(input().rstrip())

for j in range(m):
    B.add(input().rstrip())

#집합 A,B의 교집합 = A&B
result = sorted(list(A&B))

#출력
print(len(result))
print(*result, sep = '\n')