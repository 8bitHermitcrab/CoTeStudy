# 같은 숫자는 싫어


arr = [1,1,3,3,0,1,1]

answer = []
answer.append(arr[0])

for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        answer.append(arr[i])

print(answer)

# https://jokerldg.github.io/algorithm/2021/04/03/no-same-number.html