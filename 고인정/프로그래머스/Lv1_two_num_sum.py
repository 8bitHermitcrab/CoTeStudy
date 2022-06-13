# 두 개 뽑아서 더하기


# numbers = [2,1,3,4,1]
numbers = [5,0,2,7]

answer = []
temp = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        v = numbers[i] + numbers[j]
        answer.append(v)
    w = numbers[i] + numbers[i]
    answer.remove(w)

print(answer)        
answer = list(set(answer))
print(answer)
answer.sort()
print(answer)

# https://velog.io/@ckr3453/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%91%90-%EA%B0%9C-%EB%BD%91%EC%95%84%EC%84%9C-%EB%8D%94%ED%95%98%EA%B8%B0