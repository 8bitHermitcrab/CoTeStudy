# 랜선 자르기

k, n = map(int, input().split())

lan_list = []

for _ in range(k):
    lan_list.append(int(input()))

# print(sum(lan_list) / 11)

start = 1
end = max(lan_list)

while start <= end:
    mid = (start + end) // 2
    # 랜선 수
    lan_cnt = 0
    # 분할된 랜선 수
    for i in lan_list:
        lan_cnt += i // mid

    if lan_cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# https://claude-u.tistory.com/443

# https://fast-it.tistory.com/entry/1654%EB%B2%88-%EB%9E%9C%EC%84%A0%EC%9E%90%EB%A5%B4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC