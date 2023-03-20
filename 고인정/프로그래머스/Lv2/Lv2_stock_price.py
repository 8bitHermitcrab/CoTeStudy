# 주식가격

prices = [1, 2, 3, 2, 3]

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]:
                break
    return answer

print(solution(prices))

# https://velog.io/@letgodchan0/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%A3%BC%EC%8B%9D%EA%B0%80%EA%B2%A9

def solution(prices):
    answer=[]
    while prices:
        check=prices.pop(0)
        if any (check > i for i in prices):
            for i in prices:
                if check>i:
                    answer.append(prices.index(i)+1)
                    break
        else:
            answer.append(len(prices))
    return answer


# 진짜 빠르다...
def solution(prices):
    stack = []
    answer = [0] * len(prices)
    for i in range(len(prices)):
        while stack != [] and stack[-1][1] > prices[i]:
            past, _ = stack.pop()
            answer[past] = i - past
        stack.append([i, prices[i]])
    for i, s in stack:
        answer[i] = len(prices) - 1 - i
    return answer