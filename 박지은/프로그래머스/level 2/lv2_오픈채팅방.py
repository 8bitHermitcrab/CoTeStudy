#https://latte-is-horse.tistory.com/131

def solution(record):
    answer = []
    
    chats = [] #i[0]
    
    user = dict()
    
    for i in record:
        logs = i.split()
        chat = logs[0]
        userid = logs[1]
        if chat in ('Enter', 'Change'):
            name = logs[2]
            user[userid] = name #dictionary에 업데이트
        chats.append([chat, userid])
    
    #이부분 몰라서 검색
    for j in chats:
        #print(j)
        chat = j[0]
        userid = j[1]
        if chat == 'Enter':
            answer.append(f'{user[userid]}님이 들어왔습니다.')
        elif chat == 'Leave':
            answer.append(f'{user[userid]}님이 나갔습니다.')
        
        
    return answer