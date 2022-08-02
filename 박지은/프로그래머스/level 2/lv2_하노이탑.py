#https://blog.naver.com/whatadayy/222817280485

#규칙
    #n - 1개의 원판을 경유지로 옮긴다.
    #1번째 원판을 목적지로 옮긴다.
    #n - 1개의 원판을 목적지로 옮긴다.

hanoi = [] 
 # 원판의 개수, 처음시작하는 기둥, 중간기둥, 마지막 기둥
def move_hanoi(n, first, semi, final):
      #####start,mid,end같은 느낌으로 함수를 바라봐야한다.#####
    
    # 원판 1개
    if n == 1: 
        hanoi.append([first,final]) # 첫번째에서 세번째로 옮긴다
    # 원판 1개 아닐 때                                
    else:
        # n-1개의 원판을 첫번째에서 중간으로 옮기기
        move_hanoi(n-1,first, final, semi) 
###첫번째에서 중간으로 옮긴다. 위치가 first, semi, final인데 final위치에 semi가 들어간거
        # 1개의 원판을 첫번째에서 마지막으로 옮기기
        move_hanoi(1, first, semi, final)
        # n-1개의 원판을 중간에서 마지막으로 옮긴다
        move_hanoi(n-1, semi, first, final) 
    
    return hanoi
    
def solution(n): 
    # 첫번째 기둥에서 두 번째 기둥을 통해 세번째 기둥으로 n개의 원판을 옮긴다.
    answer = move_hanoi(n, 1,2,3) 
    return answer