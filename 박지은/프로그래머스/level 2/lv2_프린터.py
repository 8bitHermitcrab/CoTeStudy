def solution(priorities, location):
    answer = 0
    while True:
        for i in range(len(priorities)):
            if priorities[i] == max(priorities):
                priorities[i] = -1
                answer += 1
                if i == location:
                    return answer