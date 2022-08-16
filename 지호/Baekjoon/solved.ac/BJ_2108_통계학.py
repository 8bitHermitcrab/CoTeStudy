# 백준 2108번 : 통계학

# 시간초과
n = int(input())

lst = []
count_lst = [0] * n
mode_lst = []

for i in range(n):
  m = int(input())
  lst.append(m)

  if m in lst:
    count_lst[lst.index(lst[i])] += 1

  else:
    count_lst[i] += 1

m = max(count_lst)

mode_lst1 = list(filter(lambda x: count_lst[x] == m, range(len(count_lst))))

# for i in count_lst:
#   if i == m:
#     mode_lst.append(lst[count_lst.index(i)])
#     count_lst[count_lst.index(i)] = 0

for i in mode_lst1:
  mode_lst.append(lst[i])

# print(mode_lst)
print(round(sum(lst)/n))
print(sorted(lst)[n//2])
print(sorted(mode_lst)[1])
print(max(lst) - min(lst))

##############

#성공

n = int(input())

dic = {}
lst = []
mode_lst = []

for i in range(n):
  m = int(input())
  lst.append(m)

  if m not in dic:
    dic[m] = 1

  else:
    dic[m] += 1

print(round(sum(lst)/n))

lst.sort()
print(lst[n//2])

m = max(dic.values())

for k, v in dic.items():
  if v == m:
    mode_lst.append(k)

if len(mode_lst) != 1:
  mode_lst.sort()
  print(mode_lst[1])

else:
  print(mode_lst[0])

print(lst[-1] - lst[0])