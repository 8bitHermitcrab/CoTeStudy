# 최대 공약수와 최소 공배수
# 유클리드 호제법

# 2개의 자연수 또는 정식의 최대공약수를 구하는 알고리즘
# 호제법이란 말은 두 수가 서로(互) 상대방 수를 나누어(除)서 결국 원하는 수를 얻는 알고리즘을 나타낸다.
# 2개의 자연수(또는 정식) a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다.

# * GCD(Great Common Divisor)
# A,B가 주어지면
# A,B를 서로 나누어 0이 될 때까지 나머지를 구한다.

# GCD(B,A%B)
# if A%B = 0, GCD=B
# else GCD(B,A%B)

# * LCM(Least Common Multiple)
# (A*B)/GCD

def GCD(n, m):
      num= m % n
      if num != 0:
        m, n= n, num
        return(GCD(n,m)) 
      else:
        return n

def solution(n, m):
  return [GCD(n, m), int(m*n/GCD(n, m))]



# 제일 작은 수 제거하기

def solution(arr):
  arr.remove(min(arr))
  if len(arr) == 0:
    arr= [-1]
    return arr
  else:
    return arr