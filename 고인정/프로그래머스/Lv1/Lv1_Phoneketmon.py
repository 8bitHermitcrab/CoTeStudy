# 폰켓몬

# nums = [3,3,3,2,2,4]
# nums = [3, 1, 2, 3]
nums = [3,3,3,2,2,2]

def solution(nums): 
    answer = 0 
    # 중복 제거
    set_nums = len(set(nums))
    
    # 데려갈 수 있는 폰켓몬 N/2마리
    N = len(nums)
    my_mon = N // 2

    # 데려갈 수 있는 폰켓몬과 중복된 폰켓몬 수가 같을 때
    if set_nums == my_mon:
        answer = my_mon
    # 데려갈 수 있는 폰켓몬이 중복된 폰켓몬 수보다 적을 때
    elif set_nums > my_mon:
        answer = my_mon
    # 데려갈 수 있는 폰켓몬이 중복된 폰켓몬 수보다 클 때
    elif set_nums < my_mon:
        answer = set_nums
    return answer


print(solution(nums))