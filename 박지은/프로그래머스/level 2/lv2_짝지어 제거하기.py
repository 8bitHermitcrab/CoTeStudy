#https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EC%A7%9D%EC%A7%80%EC%96%B4-%EC%A0%9C%EA%B1%B0%ED%95%98%EA%B8%B0
def solution(s):
    check_lst = []
    for i in range(len(s)):
        #빈 리스트이면 추가해주기
        if not check_lst:
            check_lst.append(s[i])
        else:
            #리스트에 있는 마지막 값이랑 같으면 빼주기
            if s[i] == check_lst[-1]:  
                check_lst.pop()
            #리스트에 있는 마지막 값이랑 다르면 추가해주기
            else:
                check_lst.append(s[i])      
    
    #리스트가 비어 있지 않으면 0, 비어 있으면 1
    if check_lst :
        answer = 0               
    else :
        answer = 1                   

    return answer