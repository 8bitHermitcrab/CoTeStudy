# 동전 0

n, k = map(int, input().split())

coin = []
cnt = 0

for _ in range(n):
    # 동전의 가치 a
    coin.append(int(input()))

# print(coin)

for i in reversed(range(n)):
    # print(coin[i])
    if coin[i] > k:
        pass
    else:
        cnt += k // coin[i]
        # temp = coin[i] * cnt
        k = k % coin[i]
        # print(f'cnt = {cnt}')
        # print(f'k = {k}')

print(cnt)