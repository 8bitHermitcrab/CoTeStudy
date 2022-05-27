# 비밀지도

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

answer = []

for i in range(n):
    temp = bin(arr1[i] | arr2[i])
    # 숫자 앞에 0 붙이기
    temp = temp[2:].zfill(n)
    temp = temp.replace('1', '#').replace('0', ' ')
    answer.append(temp)




print(temp[2:].zfill(n))
temp = temp.replace('1', '#').replace('0', ' ')
print(temp)
print(answer)