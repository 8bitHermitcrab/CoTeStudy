# 백준 1929번 : 소수 구하기
m, n=map(int,input().split())

for i in range(m,n+1):
  # 1은 소수가 아니므로 제외
    if i == 1: 
        continue
    for j in range(2, int(i**0.5)+1):
      # 약수 존재
        if i%j == 0: 
            break    
    else:
        print(i)