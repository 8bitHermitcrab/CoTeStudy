# 정수 내림차순으로 배치하기

# n = int(input())
n = 118372

n_list = list(str(n))
n_list.sort(reverse=True)
answer = "".join(n_list)

# print(answer)

answer = int(answer)

print(answer)

# https://velog.io/@jokwed/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python%EC%A0%95%EC%88%98-%EB%82%B4%EB%A6%BC%EC%B0%A8%EC%88%9C%EC%9C%BC%EB%A1%9C-%EB%B0%B0%EC%B9%98%ED%95%98%EA%B8%B0