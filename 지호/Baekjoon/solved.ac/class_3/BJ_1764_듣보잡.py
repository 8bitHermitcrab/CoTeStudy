# 백준 1764번 : 듣보잡

# 출력 가능 but 시간초과
# 리스트 말고 세트로 진행한 것은 성공함..(맨 마지막 코드)
n, m = map(int, input().split())

lst = []
lst2 = []

for i in range(n+m):
  name = input()
  if name in lst:
    lst2.append(name)
  else:
    lst.append(name)

print(len(lst2))
for j in sorted(lst2):
  print(j)

#######################

# 성공
# 집합의 성질 사용
n, m = map(int, input().split())

s = set()
s2 = set()

for i in range(n):
  name = input()
  s.add(name)

for i in range(m):
  name = input()
  s2.add(name)

ss = sorted(list(s & s2))
print(len(ss))

for j in ss:
  print(j)

################

# 리스트를 세트로 바꿔서 실행한 결과 성공

n, m = map(int, input().split())

s = set()
s2 = set()

for i in range(n+m):
  name = input()
  if name in s:
    s2.add(name)
  else:
    s.add(name)

ss = sorted(s2)

print(len(ss))

for j in ss:
  print(j)


##########

# 최종 코드 (128ms)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

s = set()
s2 = set()

for i in range(n+m):
  name = input().rstrip()
  if name in s:
    s2.add(name)
  else:
    s.add(name)

ss = sorted(list(s2))
print(len(ss))

print(*ss, sep=' ')