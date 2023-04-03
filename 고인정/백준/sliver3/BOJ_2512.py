# 예산

n = int(input())
cities = list(map(int, input().split()))
budgets = int(input())  # 예산
start, end = 0, max(cities) # 시작점, 끝점

# 이분 탐색
while start <= end:
    mid = (start + end) // 2
    total = 0   # 총 지출
    for city in cities:
        if city > mid:
            total += mid
        else:
            total += city
    if total <= budgets:    # 지출이 예산보다 작으면
        start = mid + 1
    else:   # 지출이 예산보다 크면
        end = mid - 1
print(end)

# https://deep-learning-study.tistory.com/604