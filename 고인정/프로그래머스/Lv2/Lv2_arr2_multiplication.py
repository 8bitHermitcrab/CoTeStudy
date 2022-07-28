# 행렬의 곱셈

# arr1(m * k) * arr2(k * n) = arr3(m * n)

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

'''
# 3행 2열
# arr1[0][0] * arr2[0][0] + arr1[0][1] * arr2[1][0]
# arr1[1][0] * arr2[0][0] + arr1[1][1] * arr2[1][0]
# arr1[2][0] * arr2[0][0] + arr1[2][1] * arr2[1][0]

# arr1[0][0] * arr2[0][1] + arr1[0][1] * arr2[1][1]
# arr1[1][0] * arr2[0][1] + arr1[1][1] * arr2[1][1]
# arr1[2][0] * arr2[0][1] + arr1[2][1] * arr2[1][1]

#---

# arr1[0][0] * arr2[0][0] + arr1[0][1] * arr2[1][0], arr1[0][0] * arr2[0][1] + arr1[0][1] * arr2[1][1]

# arr1[1][0] * arr2[0][0] + arr1[1][1] * arr2[1][0], arr1[1][0] * arr2[0][1] + arr1[1][1] * arr2[1][1]

# arr1[2][0] * arr2[0][0] + arr1[2][1] * arr2[1][0], arr1[2][0] * arr2[0][1] + arr1[2][1] * arr2[1][1]

'''
# arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
# arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

def solution(arr1, arr2):
    arr1_row = len(arr1)
    arr1_col = len(arr1[0]) 
    # = arr2_row = len(arr2)
    arr2_col = len(arr2[0])

    answer = [[0 for _ in range(arr2_col)] for _ in range(arr1_row)]

    print(f'answer = {answer}')

    # print(arr1_row, arr1_col)
    # print(arr2_row, arr2_col)

    for i in range(arr1_row):
        for j in range(arr2_col):
            for k in range(arr1_col):
                answer[i][j] += (arr1[i][k] * arr2[k][j])

    return answer

print(solution(arr1, arr2))

# https://eda-ai-lab.tistory.com/489


 # row_list = []
    # col_list = []

    # for i in range(arr1_row):
    #     for j in range(arr2_row):
    #         row_list.append(arr1[i][j] * arr2[j][j])
    
    # print(f'row_list = {row_list}')

    # while len(row_list) != 0:
    #     col_list.append(sum(row_list[0:arr2_col]))
    #     del row_list[0:arr2_col]
    #     print(row_list)
    
    # print(f'col_list = {col_list}')
    
    # for i in range(arr1_col):
    #     for j in range(arr2_col):
    #         col_list.append(arr1[i][j] * arr2[j][j]) 