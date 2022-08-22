# 나이순 정렬

n = int(input())

age_name = []

for _ in range(n):
    (age, name) = input().split()
    age_name.append((int(age), name))

# print(age_name)

# for i in range(n):
#     print(f'{age_name[i][0]} {age_name[i][1]}')

# sort_age = [age_name.values()]
# print(f'sort_age = {sort_age}')

# for i in range(n):
#     for j in range(n-1):
#         print(sort_age[j])

sorted_list = sorted(age_name, key=lambda age : age[0])

for i in sorted_list:
    print(i[0], i[1])
    
# https://assaeunji.github.io/python/2020-05-05-bj10814/
