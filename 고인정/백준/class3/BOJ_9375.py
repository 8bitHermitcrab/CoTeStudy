# 패션왕 신해빈

t = int(input())

for i in range(t):
    n = int(input())
    clothes_dict = dict()
    for j in range(n):
        clothes = list(input().split())
        if clothes[1] in clothes_dict:
            clothes_dict[clothes[1]].append(clothes[0])
        else:
            clothes_dict[clothes[1]] = [clothes[0]]
    # 각 종류마다 항목의 개수
    cnt = 1

    for k in clothes_dict:
        print(f'cnt1 = {cnt}')
        print(f'len(clothes_dict[{k}]) = {len(clothes_dict[k])}')
        # cnt *= len(clothes_dict[k])
        # 착용을 해도 되고, 안 해도 됨
        # (a종류수 +1) * (b종류수 +1) * (c종류수 +1)...-1
        cnt *= len(clothes_dict[k])+1
        print(f'cnt2 = {cnt}')
    print(f'clothes_dict = {clothes_dict}')
    # print(f'cnt = {cnt}')
    # 모든 의상을 착용하지 않은 경우 제외
    print(f'cnt{cnt}-1 = {cnt-1}')


# print(f'clothes_dict = {clothes_dict}')
# print(f'clothes = {clothes}')


# https://hongcoding.tistory.com/60


'''
# 테스트 케이스
t = int(input())

# 의상이름()종류 개수
n = int(input())

name_category = {}
name_set = set()
stack = []

for i in range(n):
    name, category = map(str, input().split())
    if len(stack) == 0:
        stack.append(category)
        name_set.add(name)
        name_category[stack[-1]] = name_set
    else:
        if stack[-1] != category:
            name_set.add(name)
            name_category[category] = name_set
            stack.append(category)
        else:
            try:
                name_category[category] += name_set
            except:
                name_category[category] = name_set

print(name_category)
# name_set
'''

