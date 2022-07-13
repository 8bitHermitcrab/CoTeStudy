# 신규 아이디 추천

new_id = "...!@BaT#*..y.abcdefghijklm."

def solution(new_id):
    answer = ''
    # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    new_id = new_id.lower()
    # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.

    for id in new_id:
        # isalnum() : 문자, 숫자인지 판별
        if id.isalnum() or id in '-_.':
            answer += id

    # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    while '..' in answer:
        answer = answer.replace('..', '.')

    # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if answer[0] == '.': 
        if len(answer) >= 2:
            answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]

    # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if answer == '':
        answer = 'a'

    # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
        #  만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while len(answer) < 3:
        answer += answer[-1]

    return answer

print(solution(new_id))


# https://dapsu-startup.tistory.com/entry/Python-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-level1-%EC%8B%A0%EA%B7%9C-%EC%95%84%EC%9D%B4%EB%94%94-%EC%B6%94%EC%B2%9C