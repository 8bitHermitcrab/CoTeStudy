#입력
N = int(input())

#팩토리얼 구하기
num = 1
for i in range(1,N+1):
    num *= i

#n!를 문자열로 바꾸기
str_num = str(num)

#0의 개수
zero_count = 0

#끝에서부터 0의 개수 세기
for i in str_num[::-1]:
    if i == '0':
        zero_count += 1
    #0 없으면 빠져나오기
    else:
        break
#출력
print(zero_count)
