# 튜플

# {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}

# {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
# {{2, 1, 3, 4}, {2}, {2, 1, 3}, {2, 1}}
# {{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}


# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s = "{{20,111},{111}}"

def solution(s):
    answer = []
    # 맨 앞 {{ 와 맨 뒤 }}를 없애준다
    s = s[2:-2]
    # print(s)

    # split으로 리스트 만들기
    s = s.split("},{")
    print(s)

    s.sort(key = len)
    print(s)

    for i in s:
        iStr = i.split(",")
        for j in iStr:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

print(solution(s))

# https://hazung.tistory.com/103


''' 
# 아래 코드도 맞는 풀이였지만 좀 더 코드를 짧게 할 수 있는 방법을 찾아봄

def solution(s):
    answer = []
    
    s = s.replace("{", " ")
    # print(s)
    s = s.replace("}", " ")
    # print(s)

    s_list = []
    s_list = s.split(" , ")
    # print(s_list)
    temp = []
    for i in s_list:
        # print(f'i = {i}')
        i = i.strip()
        i = i.split(",")
        # print(f's_i = {i}')
        temp.append(i)
    
    print(f'temp = {temp}')
    temp.sort(key = len)
    print(f'temp = {temp}')

    num_list = []
    for list in temp:
        for num in list:
            num = int(num)
            num_list.append(num)

    print(f'num_list = {num_list}')

    for i in num_list:
        if i not in answer:
            answer.append(i)
        else:
            pass

    # print(f'answer = {answer}')        
        
    return answer


print(solution(s))

'''
