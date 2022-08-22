# 체스판 다시 칠하기

n, m = map(int, input().split())

# 칠해야될 보드판
board = []
cnt = []

for _ in range(n):
    board.append(input())

# 8부터 시작하는 인덱스
for row in range(n-7):
    for col in range(m-7):
        # W로 시작할 경우의 바뀐 개수
        indexW = 0
        # B로 시작할 경우
        indexB = 0 

        # 0~7 = 8칸
        for i in range(row, row+8):
            for j in range(col, col+8):
                # 합이 짝수면 시작점과 같은 색깔
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        indexW += 1
                    if board[i][j] != 'B':
                        indexB += 1
                # 합이 홀수면 시작점과 다른 색깔이어야함
                else:
                    if board[i][j] != 'B':
                        indexW += 1
                    if board[i][j] != 'W':
                        indexB += 1
        print(f'indexW = {indexW}')
        print(f'indexB = {indexB}')
        # cnt.append(min(indexW, indexB))
        cnt.append(indexW)
        cnt.append(indexB)

print(cnt)
print(min(cnt))



# https://bambbang00.tistory.com/43