#https://velog.io/@kauthenticity/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%95%A0%EC%9D%B8-%ED%96%89%EC%82%AC-python
def solution(want, number, discount):
    answer = 0
    
    
    wish = {} # 내가 갖고 싶은 거
    cur = {} # 10일 전부터 오늘까지 가질 수 있는 물건들
    
    for i in range(len(want)) :
        #내가 갖고 싶은 물건이 key, 수량이 value
        wish[want[i]] = number[i]
        #10일 전부터 오늘 전까지 가질 수 있는 물건이 key, 그 수량이 value
        cur[want[i]] = 0
    
    #discount를 처음부터 돌면서 할인하는 물건이 내가 갖고 싶은 물건이면 cur 사전에서 수량을 증가시킨다. 그리고, 10일이 지난 물건은 cur 사전에서 삭제시킨다.
    #cur사전에 있는 모든 물건의 수량이 wish 물건의 수량 이상이면 살 수 있으므로 answer를 1 증가시킨다
    for i in range(len(discount)) :     
        before = i - 10
        
        # 10일 전 상품 삭제
        if discount[before] in want and before >= 0 : 
            if cur[discount[before]] > 0 : 
                cur[discount[before]] -= 1
        
        if discount[i] in want:
            cur[discount[i]] += 1
            
        canBuy = True
        
        for key in wish.keys() :
            if wish[key] > cur[key] : 
                canBuy = False
                break
        if canBuy is True: 
            answer += 1
            
        
    return answer