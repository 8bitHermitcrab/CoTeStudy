#이렇게 접근하는거 아닌거같다ㅏㅏㅏ
# def solution(s):
#     answer = []
#     temp = []
#     for i in s:
#         if i == '{':
#             continue
#         elif i == '}':
#             continue
#         elif i == ',':
#             continue
#         else:
#             temp.append(int(i))
            
#     return 



#https://hazung.tistory.com/103

def solution(s):
    # 맨앞 '{{'와 맨뒤 '}}'를 잘라준다. 그리고 '},{'을 기준으로 split하면 괄호문자가 모두 사라진다.
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    #print(s)
    # s는 현재 ','를 포함한 문자열 원소들이다. 👉[ '1', '1,2', '1,2,3' ]
    
    # 정렬
    s.sort(key = len)
    
    # 반복문에 들어오는 원소마다 ','을 기준으로 split해준다. 👉[ '1, 2' ]가 들어온다면 [ '1', '2' ]로 만든다.
    for i in s:
        ii = i.split(',')
        #print(ii)
        # answer 배열에 차례대로 append해준다.
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
                #print(answer)
    return answer