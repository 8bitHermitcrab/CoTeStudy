# 크레인 인형뽑기 게임


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

box = []
answer = []

for move in moves:
    for i in range(len(board)):
        # print(f'board[{i}][{move}-1] = {board[i][move-1]}')
        if board[i][move-1] > 0:
            print(f'board[{i}][{move}-1] = {board[i][move-1]}')
            box.append(board[i][move-1])
            print(f'box = {box}')
            print(f'board1 = {board}')
            board[i][move-1] = 0
            print(f'board2 = {board}')
            if box[-1:] == box[-2: -1]:
                answer += box[-1:]
                box = box[:-2]
            break
print(answer)
print(box)



# v_list = []

# for move, value in box.items():
#     v_list.append(value)

# https://velog.io/@matisse/%EC%B9%B4%EC%B9%B4%EC%98%A4-%ED%81%AC%EB%A0%88%EC%9D%B8-%EC%9D%B8%ED%98%95-%EB%BD%91%EA%B8%B0-python