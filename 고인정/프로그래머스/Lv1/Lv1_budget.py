# 예산

d = [1,3,2,5,4]
budget = 9

answer = 0
d.sort()
for i in range(len(d)):
    if budget >= d[i]:
        budget -= d[i]
        answer += 1

print(answer)


# https://it-garden.tistory.com/233