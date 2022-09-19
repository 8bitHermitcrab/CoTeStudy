def solution(n):
    #n을 2진수로 바꾸기
    n_2 = bin(n)
    n_2_str = str(n_2)
    #n을 2진수로 바꿨을 때 1의 갯수
    n_2_1num = n_2_str.count('1')
    
    x = n
    while True:
        #x를 1씩 증가시키면서
        x += 1
        #2진수에서
        x_2 = bin(x)
        x_2_str = str(x_2)
        #1의 갯수 세주기
        x_2_1num = x_2_str.count('1')
        
        #n이랑 x 2진수에서 1의 갯수가 같으면 정답, while문 빠져나오기
        if n_2_1num == x_2_1num:
            answer = x
            break
        
        #1의 갯수가 같지 않으면 계속 진행
        else:
            continue
    
    
    return answer