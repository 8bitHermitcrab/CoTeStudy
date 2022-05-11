# 하샤드 수

x = 13
# x_10 = x // x

str_x = str(13)
x_list = []

for i in range(len(x)):
    x_list.append(i)

print(x_list)

# for i in range(x_list[0], len(x_list)+1):
#     x_list[0] // x_list[i]

if sum(x_list) == x :
    answer = True
else :
    answer = False

print(answer)