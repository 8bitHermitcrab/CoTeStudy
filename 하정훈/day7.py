# 정수 내림차순으로 배치하기

def solution(n):
    num= list(str((int(n))))
    print(num)
    num.sort()
    num.reverse()
    return int(''.join(num))


# 다른 풀이

def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

# 자연수 뒤집어 배열로 만들기
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

def solution(n):
    num= list(str((int(n))))
    num.reverse()
    ls= []
    for i in num:
      i=int(i)
      ls.append(i)
    return ls

def digit_reverse(n):
    return list(map(int, reversed(str(n))))

def digit_reverse(n):
    return list(map(int, list(str(n))[::-1]))

# 다른 풀이

def solution(n):
    num= list(map(int,str(n)))
    a= 0
    for i in num:
      a += i
    return a

def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10) 

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));

