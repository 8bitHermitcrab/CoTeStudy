# 영어 끝말잇기

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

def solution(n, words):
    answer = [0, 0]
    stack = [words[0]]
    print(f'stack = {stack}')
    for i in range(1, len(words)):
        if stack[-1][-1] == words[i][0] and words[i] not in stack:
            stack.append(words[i])
            print(f'stack = {stack}')
            print(f'stack[-1][-1] = {stack[-1][-1]}')
            print(f'words[{i}] = {words[i]}')
            print(f'words[{i}][0] = {words[i][0]}')
        else:
            print(f'i = {i}')
            print(f'(i % n) = {i % n}')
            print(f'(i // n) = {i // n}')
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1
            break
    return answer


print(solution(n, words))

# https://wiselog.tistory.com/85

'''
def solution(n, words):
    # 번호, 차례
    answer = [0, 0]
    num = [n for _ in range(n+1)]
    print(f'num = {num}')
    person = 

    # people_words = [[] * (n+1) for _ in range(n+1)]
    people_words = []

    print(words)

    for i in range(0, len(words), n):
        print(f'words[{i}:{n}] = {words[i:n]}')
        print(f'words[{n}:{len(words) - n}] = {words[n:len(words) - n]}')
        print(f'words[{len(words) - n}:] = {words[len(words) - n:]}')

    print(people_words)

    return answer

print(solution(n, words))
'''