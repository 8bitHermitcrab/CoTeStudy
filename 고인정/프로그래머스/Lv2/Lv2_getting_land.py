# 땅따먹기

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            # print(f'land[{i-1}][:{j}] = {land[i-1][:j]}')
            # print(f'land[{i-1}][{j+1}:] = {land[i-1][j+1:]}')
            # print(f'land[i-1][:j] + land[i-1][j+1:] = {land[i-1][:j] + land[i-1][j+1:]}')
            # print(f'land[i][j] = land[{i}][{j}] = {land[i][j]}')
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
            # print(f'### land[i][j] = land[{i}][{j}] = {land[i][j]} ###')
    
    # print(land)
    # 마지막 행의 인덱스이기 때문에 -1 해줘야함
    return max(land[len(land) - 1])

# https://velog.io/@ansrjsdn/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EB%95%85%EB%94%B0%EB%A8%B9%EA%B8%B0-python

'''
def solution(land):
    answer = 0

    # land[0][0] = 1
    # land[0][3] = 5
    
    for i in range(len(land)):
        print(f'max(land[i]) = {max(land[i])}')
        # answer += max(land[0])
        if i > 0:
            if max(land[i]) == land[i][3]:
                print(land[i][3])
                del land[i][3]
                print(f'land = {land}')
                answer += max(land[i])
            else:
                answer += max(land[i])
        else:
            answer += max(land[i])

    return answer
'''
print(solution(land))