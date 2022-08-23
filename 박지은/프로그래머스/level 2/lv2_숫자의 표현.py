def solution(n):
    answer = 0
    #1부터 n까지 돌어가면서
    for i in range(1, n+1):
        num_sum = 0
        
        #n보다 합이 작을 경우에 while문 돌리기
        while num_sum < n:
            num_sum += i
            i += 1
            
        #while문 빠져나와서 합이 n이랑 같으면 1씩 +
        if num_sum == n:
            answer += 1
        #while문 빠져나와서 합이 n보다 큰 경우(답 아닌 경우)
        else:
            continue

    return answer