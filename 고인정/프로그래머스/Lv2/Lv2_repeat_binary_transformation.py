# 이진 변환 반복하기

s = "110010101001"
# s = '1111111'

def solution(s):
    # 2진 변환 횟수
    cnt_base2 = 0
    # 제거된 0의 개수
    cnt_0 = 0

    while len(s) > 1:
        ones = s.count('1')
        # print(f'one = {ones}')
        cnt_0 += s.count('0')
        # print(f'cnt_0 = {cnt_0}')
        s = str(bin(ones))[2:]
        # print(f's = {s}')
        cnt_base2 += 1
        # print(f'cnt_base2 = {cnt_base2}')

    answer = [cnt_base2, cnt_0]
    
    return answer

print(solution(s))