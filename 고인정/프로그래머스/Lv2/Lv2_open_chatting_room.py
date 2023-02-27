# 오픈채팅방

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

def solution(record):
    answer = []
    id_nick = dict()
    for i in record:
        status = i.split()
        if len(status) == 3:
            id_nick[status[1]] = status[2]
    for i in record:
        status = i.split()
        if status[0] == 'Enter':
            answer.append('%s님이 들어왔습니다.' %id_nick[status[1]])
        elif status[0] == 'Leave':
            answer.append('%s님이 나갔습니다.' %id_nick[status[1]])
    print('id_nick', id_nick)
    return answer

print(solution(record))

# https://velog.io/@godiva7319/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2-%EC%98%A4%ED%94%88%EC%B1%84%ED%8C%85%EB%B0%A9-Python