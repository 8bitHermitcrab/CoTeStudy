### 문자열을 정수로 바꾸기 ###
# 문제 설명
# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.

# 제한 조건
# s의 길이는 1 이상 5이하입니다.
# s의 맨앞에는 부호(+, -)가 올 수 있습니다.
# s는 부호와 숫자로만 이루어져있습니다.
# s는 "0"으로 시작하지 않습니다.

# 입출력 예
# 예를들어 str이 "1234"이면 1234를 반환하고, "-1234"이면 -1234를 반환하면 됩니다.
# str은 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.

def solution(s):
    answer= int(s)
    return answer

### 수박수박수박? ###
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 
# 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

# 제한 조건
# n은 길이 10,000이하인 자연수입니다.

# 입출력 예
# n	return
# 3	"수박수"
# 4	"수박수박"

def solution(n):
    fst= '수'
    sec= '박'
    answer= ''
    for i in range(1, n+1):
      if i % 2 == 0:
        answer += sec
      else:
        answer += fst
    return answer

# 다른 풀이

def water_melon(n):
    s = "수박" * n
    return s[:n]


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));

def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));


### 소수 찾기 ###
# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.
# 입출력 예
# n	result
# 10	4
# 5	3
# 입출력 예 설명
# 입출력 예 #1
# 1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

# 입출력 예 #2
# 1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

def solution(n):
  count= 0
  for n in range(2, n+1):
    for i in range(2, n):
      if n % i == 0:
        break
    else:
      count += 1
  return count