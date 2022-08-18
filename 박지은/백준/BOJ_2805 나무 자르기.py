#220819

#1. 절단기에 높이 H를 지정
#2. 톱날이 땅으로부터 Hm 위로 올라가 그 위에 있는 나무 모두 절단
#3. 나무를 필요한 만큼만(최소로) 집으로 가져가려고 한다.
#4. H의 최댓값 구하기 

###입력
# 첫째 줄에 나무의 수 N과 필요한 나무의 길이 M
# 둘째 줄에 가져가려는 나무의 길이

###출력
# 적어도 M미터의 나무를 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값



#############시간초과######################
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

namu = list(map(int, input().split()))

H = 0
check = 0
while check != 1:
    namu_cut = []
    H += 1
    for i in namu:
        x = i - H #잘린 나무의 길이

        #나무의 길이가 H보다 같거나 작은 경우
        if x<=0:
            continue
        else:
            namu_cut.append(x)
 
    if sum(namu_cut) <= M:
        check = 1
    else:
        namu_cut2 = sum(namu_cut)

print(H)


###################이것도 시간초과ㅏㅏㅏㅏㅏㅏ###############################

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

namu = list(map(int, input().split()))

H = 0

# H를 1씩 증가시키면서 나무 자르기
while True:
    namu_cut = 0
    print(f'H = {H}')
    for i in namu:
        # 나무의 길이가 H보다 같거나 작으면 (안잘림)
        if i <= H:
            x = 0 
        # 나무의 길이가 H보다 길면 (잘림)
        else:
            x = i-H #잘린 나무 길이
            namu_cut += x 
        print(f'x = {x}')
        
    print(f'namu_cut = {namu_cut}')
    if namu_cut <= M:
        break
    else:
        H += 1

print(H)


###############이분 탐색###################
#https://blog.naver.com/tladhehd/222801003561

# min_H는 최소, max_H는 최대, mid는 중간점
# M보다 커지면 반복문 빠져나오기
# min_height를 1씩 늘리고 max_height를 1씩 감소시켜 탐색범위를 좁혀가며 진행

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

namus = list(map(int, input().split()))

min_H = 0
max_H = max(namus)

answer = 0

while min_H <= max_H:
    
    mid = (min_H + max_H)//2 #중간 위치
    num = 0

    for namu in namus:
        if namu > mid:
            num += namu - mid
        if num >= M:
            break
    if num >= M:
        answer = max(answer, mid)
        min_H = mid + 1
    else:
        max_H = mid - 1
print(answer)

#시간 : 3476ms


#이분 탐색 알고리즘
#https://blog.naver.com/eunaii9/222205212553
##크기 순으로 정렬되어 있는 리스트에서 사용할 수 있는 탐색 방법
##리스트를 먼저 둘로 나누고, 중간 자료를 기준으로 더 작은 쪽이나 큰 쪽을 선택하여 원하는 값을 탐색