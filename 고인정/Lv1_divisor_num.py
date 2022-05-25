# 나누어 떨어지는 숫자 배열

arr = [5, 9, 7, 10]
divisor = 5


answer = []

for i in arr:
    if i % divisor == 0:
        answer.append(i)

if len(answer) == 0:
    answer = [-1]

answer.sort()


# https://velog.io/@whgurwns2003/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%82%98%EB%88%84%EC%96%B4-%EB%96%A8%EC%96%B4%EC%A7%80%EB%8A%94-%EC%88%AB%EC%9E%90-%EB%B0%B0%EC%97%B4level-1-%ED%92%80%EC%9D%B4python%ED%8C%8C%EC%9D%B4%EC%8D%AC