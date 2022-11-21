# 기능 개발

progresses = [93, 30, 55]
speeds = [1, 30, 5]

# progresses = [95, 90, 99, 99, 80, 99]
# speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    answer = []
    time = 0
    cnt = 0

    while len(progresses) > 0:
        # print(f'time = {time}, cnt = {cnt}, progresses = {progresses}')
        if (progresses[0] + time * speeds[0]) >= 100:
            # print(f'progresses = {progresses}')

            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
            # print(f'cnt = {cnt}')

        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            time += 1

    answer.append(cnt)
    return answer

print(solution(progresses, speeds))

# https://huidea.tistory.com/15

'''
def solution(progresses, speeds):
    answer = []
    
    time = 0
    cnt = 0

    # finish = []

    # for i in range(len(speeds)):
    #    finish.append(((100 - progresses[i]) // speeds[i]))

    # print(f'finish = {finish}')
'''

'''
def solution(progresses, speeds):
    answer = []

    finish = []

    for i in range(len(speeds)):
       finish.append(((100 - progresses[i]) // speeds[i]))

    print(f'finish = {finish}')

    # 구현 완료된 기능
    cnt = 0
    stack = [0] * (len(finish) + 1)

    j = 1
    while len(stack)-1 != j:
        f = finish[0]
        stack[j] = finish[j] - f
        print(f'stack[{j}] = {stack[j]}')
        cnt += 1
        finish.pop(0)
        j += 1


    print(f'stack = {stack}')
    print(f'finish2 = {finish}')
        # finish = [5, 10, 1, 1, 20, 1]
        #           1         3      2
        #           0, 5, -4, -4, 15, -4
        # finish.pop(0)
        # cnt += 1

    return answer

print(solution(progresses, speeds))
'''