# 최댓값과 최솟값

s = "-1 -2 -3 -4"

def solution(s):
    answer = ''
    s_list = s.split()
    s_list_int = list(map(int, s_list))
    s_list.sort()
    # print(s_list_int)
    answer = str(min(s_list_int)) + ' ' + str(max(s_list_int))
    return answer

print(solution(s))