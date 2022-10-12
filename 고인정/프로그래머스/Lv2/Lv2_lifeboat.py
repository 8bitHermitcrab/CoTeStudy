# 구명보트

people = [70, 50, 80, 50]
# people = [70, 80, 50]
# people = [20, 30, 50, 60]
limit = 100

def solution(people, limit):
    people.sort()
    print(f'people = {people}')
    answer = 0
    i, j = 0, len(people)-1

    while i <= j:
        print(f'i = {i}, j = {j}, answer = {answer}')
        answer += 1
        print(f'people[{j}] + people[{i}] = {people[j]} + {people[i]} = {people[j] + people[i]}')
        if people[j] + people[i] <= limit:
            i += 1
            print(f'i = {i}')
        j -= 1
        print(f'j = {j}')

    return answer

print(solution(people, limit))

# https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-in-python

'''
def solution(people, limit):
    answer = 0
    stack = []

    for i in range(len(people)):
        temp = limit - people[i]
        print(f'i = {i}, people[i] = {people[i]}, temp = {temp}')
        stack.append(temp)
        print(f'stack = {stack}')
        answer += 1
    
    for i in stack:
        if i in people:
            answer -= 1

    return answer+1

print(solution(people, limit))
'''