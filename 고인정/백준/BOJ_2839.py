# 설탕 배달

n = int(input())

bag = [5, 3]
cnt = 0

while n >= 0:
    if n % bag[0] == 0:
        print(f'n // bag[0] = {n // bag[0]}')
        print(f'cnt = {cnt}')
        cnt += n // bag[0]
        print(f'cnt = {cnt}')
        break
    n -= 3
    cnt += 1

print(-1)
