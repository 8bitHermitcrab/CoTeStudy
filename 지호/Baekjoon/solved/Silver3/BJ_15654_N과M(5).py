# 백트레킹, 재귀함수 문제!

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
answer = []
used = [False] * n

def backtracking(count): 

  for i in range(n):
    if count == m:
      print(' '.join(map(str, answer)))
      return  
      
    if not used[i]:
      answer.append(lst[i])
      used[i] = True

      backtracking(count + 1)

      answer.pop()                # 리턴으로 돌아오면 여기서 부터 실행됨 
      used[i] = False

backtracking(0)