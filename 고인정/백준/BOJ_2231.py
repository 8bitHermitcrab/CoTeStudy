# 분해합

n = int(input())
answer = 0

for i in range(1, n+1):
    a = list(map(int, str(i)))
    print(f'i = {i}')
    print(f'a = {a}')
    answer = i + sum(a)
    print(f'answer = {answer}')
    if answer == n:
        print(f'i = {i}')
        break

    if i == n:
        print(0)




# https://yongku.tistory.com/787


# 경태님 코드
n=int(input())
print(min([i for i in range(max(n-len(str(n))*9,1),n) if n == i+sum([int(j) for j in str(i)])]or[0]))


# 지호님 코드
N = int(input())

ans = []

for i in range(1, N+1):
  lst = list(map(int, str(i)))
  # print(lst)
  if (N // i == 1) & (N % i == sum(lst)):
    ans.append(i)
    # break

# print(ans)
if N>18 or N%2==1:
  try:
      print(min(ans))
  except:
      print(0)
elif N%2==0:
      print(N//2)
else: 
      print(0)