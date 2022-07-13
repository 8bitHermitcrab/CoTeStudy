# 콜라츠 추측

def solution(num):
  Repe= 0
  if num == 1:
    return 0
  while True:
    if num % 2 == 0:
      num= int(num/2)
      Repe+=1
    else:
      num= (num*3)+1
      Repe+=1
    if num == 1:
      return Repe
    if Repe > 500:
      return -1
      