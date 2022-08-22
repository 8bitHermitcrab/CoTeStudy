# 통계학

import sys

n = int(sys.stdin.readline())

num_list = []
num_dict = dict()

for _ in range(n):
    num = int(sys.stdin.readline())
    num_list.append(num)

    try: 
        num_dict[num] += 1
    except:
        num_dict[num] = 1  

# print(num_list)
# print(num_dict)

# 산술평균
# print("산술평균")
# print(sum(num_list) // len(num_list))
print(round(sum(num_list) / n))

# 중앙값
num_list.sort()
# print("중앙값")
print(num_list[len(num_list) // 2])

# 최빈값
# num_dict_sorted = sorted(num_dict.keys())
# for key, value in sorted(num_dict.items()):
    # print(key, ":", value)
    # num_dict_sorted = []
    # n = [key, value]
    # num_dict_sorted.append(n)
# print(f'num_dict_sorted = {num_dict_sorted}')

most = max(num_dict.values())
max_list = []
for key, value in num_dict.items():
    if most == value:
        max_list.append(key)
# print(max_list)
max_list.sort()
# print("최빈값")
if len(max_list) > 1:
    print(max_list[1])
else:
    print(max_list[0])

# 범위
# ran = max(num_list) - min(num_list)
ran = num_list[-1] - num_list[0]
# print("범위")
print(ran)


# https://always-challenger-lab.tistory.com/11
# https://rfriend.tistory.com/473