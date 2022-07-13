# [카카오 인턴] 키패드 누르기


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
'''

def solution(numbers, hand):
    key_pad = {1:[0, 0], 2:[0, 1], 3:[0, 2],
                4:[1, 0], 5:[1, 1], 6:[1, 2],
                7:[2, 0], 8:[2, 1], 9:[2, 3],
                '*':[3, 0], 0:[3, 1], '#':[3, 2]}


    answer = ""
    # 시작 위치
    L_hand = key_pad["*"]
    R_hand = key_pad["#"]

    for i in numbers:
        now = key_pad[i]
        if i in [3, 6, 9]:
            answer += "R"
            R_hand = now
        elif i in [1, 4, 7]:
            answer += "L"
            L_hand = now
        else:
            # 왼손/오른손 거리
            L_dist = 0
            R_dist = 0

            # 거리 계산하기
            for l, r, n in zip(L_hand, R_hand, now):
                L_dist += abs(r - n)
                R_dist += abs(l - n)
                # print(f'now = {now}, L_dist = {L_dist}')
                # print(f'now = {now}, R_dist = {R_dist}')

            if L_dist > R_dist:
                R_hand = now
                answer += "R"
            elif L_dist < R_dist:
                L_hand = now
                answer += "L"
            else:
                if hand == "right":
                    answer += "R"
                    R_hand = now
                else:
                    answer += "L"
                    L_hand = now

    return answer

# print(distance(1, 3))'''

def Distance(handNum, nextNum):
    keypad = {1: [0, 0], 2: [1, 0], 3: [2, 0],
              4: [0, 1], 5: [1, 1], 6: [2, 1],
              7: [0, 2], 8: [1, 2], 9: [2, 2],
              "*": [0, 3], 0: [1, 3], "#": [2, 3], }

    x1, y1 = keypad[handNum]
    x2, y2 = keypad[nextNum]

    return abs(x1-x2) + abs(y1-y2)


def solution(numbers, hand):
    answer = ''
    left = "*"
    right = "#"

    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left = number
        elif number in [3, 6, 9]:
            answer += "R"
            right = number
        else:
            leftDist = Distance(left, number)
            rightDist = Distance(right, number)

            if leftDist < rightDist:
                answer += "L"
                left = number
            elif rightDist < leftDist:
                answer += "R"
                right = number
            else:
                if hand == "left":
                    answer += "L"
                    left = number
                else:
                    answer += "R"
                    right = number

    return answer


print(solution(numbers, hand))

# https://bladejun.tistory.com/115

# https://kyoung-jnn.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%ED%82%A4%ED%8C%A8%EB%93%9C-%EB%88%84%EB%A5%B4%EA%B8%B0