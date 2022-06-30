# 단어 정렬

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로

n = int(input())

str_list = []

for i in range(n):
    str_list.append(input())

# 중복 제거 리스트
set_list = list(set(str_list))
print(f'set_list = {set_list}')

# 정렬
sort_list = []
for j in set_list:
    sort_list.append((len(j), j))
print(f'sort_list = {sort_list}')
    
answer = sorted(sort_list)

for k, word in answer:
    print(word)
