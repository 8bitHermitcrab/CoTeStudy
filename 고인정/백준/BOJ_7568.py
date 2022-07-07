# 덩치

n = int(input())

kg_cm = []

for _ in range(n):
    kg, cm = map(int, input().split())
    kg_cm.append((kg, cm))

for i in kg_cm:
    rank = 1
    for j in kg_cm:
        # 몸무게         와   키 비교
        if i[0] < j[0] and i[1] < j[1]:
        # 몸무게와 키가 작으면 랭크+1
            rank += 1
    print(rank, end=' ')