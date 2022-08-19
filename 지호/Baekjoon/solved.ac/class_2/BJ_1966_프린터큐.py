# 백준 1966번 : 프린터큐

# 딕셔너리 접근 (리스트 보다 빠름)

N = int(input())

for _ in range(N):
  answer = 0  
  n, m = map(int, input().split())
  id = range(n)
  imp = dict(zip(id, list(map(int, input().split()))))
  imp_lst = list(zip(imp.values(), imp.keys()))

  while True:
    if imp_lst[0][0] == max(imp_lst)[0]:
      answer += 1

      if imp_lst[0][1] == m:
        print(answer)
        break

      else:
        imp_lst.pop(0)

    else:
      imp_lst.append(imp_lst.pop(0))


# 리스트 접근

N = int(input())

for _ in range(N):
  answer = 0  
  n, m = map(int, input().split())
  queue = list(map(int, input().strip().split()))
  queue = [(v, idx) for idx, v in enumerate(queue)]

  while True:
    if max(queue)[0] == queue[0][0]:
        answer += 1

        if queue[0][1] == m:
            print(answer)
            break

        else:
            queue.pop(0)

    else:
        queue.append(queue.pop(0))