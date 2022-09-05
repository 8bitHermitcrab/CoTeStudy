#https://blog.naver.com/idmanddang/222756348559
#수열의 점화식

# n칸을 뛰기 위한 경우의 수 = n-1칸을 뛰기 위한 경우의수 + n-2칸 뛰기 위한 경우의 수
# f(n) = f(n-1) + f(n-2)

#0칸 -> 1개
#1칸 -> 1개 (1)
#2칸 -> 2개 (1,1) (2)
#3칸 -> 3개 (1, 1, 1) (1. 2) (2, 1)
#4칸 -> 5개 (1, 1, 1, 1) (2, 1, 1) (1, 2, 1) (1, 1, 2) (2, 2)
#5칸 -> 8개 (1, 1, 1, 1, 1) (2, 1, 1, 1) (1, 2, 1, 1) (1, 1, 2, 1) (1, 1, 1, 2)
            #(1, 2, 2) (2, 1, 2) (1, 2, 2)


def solution(n):
    #1칸, 2칸인 경우 미리 리스트에 넣어주기
    result_list = [1, 2]
    
    #n번까지 while문 돌아가면서 result list에 전꺼, 전전꺼 값 추가해 주기
    while len(result_list) < n:
        result_list.append(result_list[-1] + result_list[-2])
    answer = result_list[n-1]%1234567

    return answer