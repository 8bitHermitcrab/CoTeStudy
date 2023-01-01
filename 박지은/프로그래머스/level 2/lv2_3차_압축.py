# 문제 이해 아직 못했어여ㅜㅜㅜ
# #https://velog.io/@hope1213/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%95%95%EC%B6%95-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# def solution(msg):
#     answer = []
#     # 1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화 한다.
#     #   dic이라는 사전을 만들어 해당 모든 알파벳을 사전에 넣는다
#     dic = {}
#     for i in range(1, 27):
#         dic[chr(i+64)] = i
    
#     # 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
#     #   현재 입력과 일치하는 가장 긴 문자열을 찾아야 하므로 입력 문자열이 "KAKAO"일 경우 kAKAO -> KAKA -> KAK -> KA -> K 순서로 사전에 해당 문자열이 있는지 찾는다.
#     while 1:        
#         if i >= len(msg):
#             break
#         for j in range(len(msg), i, -1):
#             if msg[i:j] in dic:
#             #print(msg[i:j])
#     # 3. w에 해당하는 사전의 index 번호를 출력하고, 입력에서 w를 제거한다.
#     # 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다. / 단계 2로 돌아간다
#     #   찾은 문자열을 answer라는 리스트에 넣고 (사전의 색인 번호를 출력) 찾은 문자열을 입력에서 제거한다 했으니 해당 문자열을 다시 찾지 않도록 인덱스를 증가 시켜줌
#     #   만약 "KA"라는 문자열을 찾았다면 "KAK"라는 문자열은 찾지 못했다는 의미이므로 "KAK" 문자열을 사전에 등록해준다.
#                 answer.append(dic[msg[i:j]]) #출력
#                 dic[msg[i:j+1]] = len(dic)+1 #사전 등록
#                 i = j-1 #인덱스 증가
#         i+=1
#     return answer


def solution(msg):
    answer = []
    #1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
    dic={}
    for i in range(1,27):
        dic[chr(i+64)]=i
    i=0
    
    
    while 1:
        
        # 반복문 빠져나오기
        if i >=len(msg):
            break
        
        #2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 찾기
        for j in range(len(msg),i,-1):
            if msg[i:j] in dic:
                # 3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
                # 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다
                answer.append(dic[msg[i:j]])
                dic[msg[i:j+1]] = len(dic)+1
                i=j-1
        i+=1
    return answer