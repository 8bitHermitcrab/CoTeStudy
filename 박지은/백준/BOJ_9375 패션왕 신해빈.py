#https://blog.naver.com/doju00/222758060502

#종류 별 개수를 입력 받은 후 모든 경우 구하기 -> 알몸인 경우 제외

import sys
input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    
    #옷의 개수
    n = int(sys.stdin.readline().rstrip())
    
    #옷 종류 리스트
    kind_set=[0]*n

    #각 종류에 따른 물건의 개수 세는 dictionary
    kind_count = {}

    #옷의 개수만큼 반복
    for i in range(n):
        
        #옷 입력
        name, kind = input().split()

        #옷 종류 리스트에 입력
        kind_set[i] = kind

        #옷의 종류가 딕셔너리에 없으면
        if kind not in kind_count:
            #2부터인 이유: 포함되지 않는 경우 고려
            kind_count[kind] = 2
        
        #딕셔너리에 의상이 있으면 하나 추가
        else:
            kind_count[kind] += 1
    
    #종류 중복 제거
    kind_set = set(kind_set)
    
    #입을 수 있는 경우의 수
    count = 1

    for j in kind_set:
        count *= kind_count[j]
    
    #알몸 제외
    print(count-1)