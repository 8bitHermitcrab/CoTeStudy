# 프로그래머스 압축

msg = 'TOBEORNOTTOBEORTOBEORNOT'

def solution(msg):
    answer = []
    msg_dict = {}

    for i in range(26):
        msg_dict[chr(65 + i)] = i + 1

    w, c = 0, 0
    while True:
        c += 1
        if c == len(msg):
            answer.append(msg_dict[msg[w:c]])
            break
        if msg[w:c+1] not in msg_dict:
            msg_dict[msg[w:c+1]] = len(msg_dict) + 1
            answer.append(msg_dict[msg[w:c]])
            w = c

    return answer


print(solution(msg))

# https://hazung.tistory.com/89