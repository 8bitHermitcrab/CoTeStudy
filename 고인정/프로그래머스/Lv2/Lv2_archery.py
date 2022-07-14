# 양궁대회

n = 5
info = 	[2,1,1,1,0,0,0,0,0,0,0]

def solution(n, info):

    answer = [0] * 11
    ryan_target = [0] * 11
    maxDiff = 0


    # 모든 부분 집합에 대해서 구하기
    # 10진수 = 1024, 1 ~ 1023
    for subset in range(1, 1 << 10):
        ryan = 0
        apeach = 0
        # 화살의 개수
        cnt = 0

        # 0을 제외한 10까지 인덱스
        for i in range(10):
            if subset & (1 << i):
                ryan += (10 - i)
                # 라이언 과녁에 맞춘 게 어피치 과녁에 맞춘 것보다 1 많아야함
                ryan_target[i] = info[i] + 1
                # 라이언이 쏜 화살의 개수
                cnt += ryan_target[i]
            else:
                ryan_target[i] = 0
                if info[i]:
                    apeach += (10 - i)
            
        if cnt > n:
            continue
            
        # 0점 과녁에 남아있는 화살 개수 넣기
        ryan_target[10] = n - cnt

        # 가장 낮은 점수를 맞힌 개수가 같은 경우에
        if ryan - apeach == maxDiff:
            # 0점 화살 개수 확인
            for j in reversed(range(11)):
                if ryan_target[j] > answer[j]:
                    maxDiff = ryan - apeach
                    answer = ryan_target[:]
                    break
                elif ryan_target[j] < answer[j]:
                    break

        # 라이언이 이겼을 때 차이
        elif ryan - apeach > maxDiff:
            maxDiff = ryan - apeach
            answer = ryan_target[:]

    if maxDiff == 0:
        answer = [-1]
    return answer

print(solution(n, info))


# https://www.youtube.com/watch?v=dzncNbPMiB4&t=1199s

# https://osnim.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%96%91%EA%B6%81%EB%8C%80%ED%9A%8C-%ED%8C%8C%EC%9D%B4%EC%8D%AC


# for i in range(11):

#     # 10점에 n개 맞히면 어피치가 승
#     if info[0] == n:
#         answer = [-1]

#     #
#     else:

# for i in range(11):
#     print(f'i = {i}')
#     score += (info[i] * (10-i))


# if info[0] == n:
#     result = [-1]


# print(score)
