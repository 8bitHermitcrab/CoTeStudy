# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    lst= []
    for i in range(1, n+1):
        lst.append(x*i)
        

    return lst

# 휴대폰 번호 가리기

def solution(phone_number):
    
    answer= '*'*(len(phone_number[:-4]))+phone_number[-4:]
    return answer

# 하샤드의 수

def solution(x):
  lst= []
  for i in str(x):
    lst.append(int(i))
    num_sum= sum(lst)
    num_div= x % num_sum == 0
  return num_div


  def solution(arr):
    for i in arr:
      a+=i
    answer= a % len(arr)
    return answer