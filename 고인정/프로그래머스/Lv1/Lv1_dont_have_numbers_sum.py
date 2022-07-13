# 없는 숫자 더하기

numbers = [1, 2, 3, 4, 6, 7, 8, 0]

def solution(numbers):
    answer = 0
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers.sort()
    
    for i in range(len(numbers)):
        if numbers[i] in nums:
            nums.remove(numbers[i])

    return sum(nums)


print(solution(numbers))