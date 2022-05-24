# 문자 내 마음대로 정렬하기

strings = ["abce", "abcd", "cdx"]
# strings = ["sun", "bed", "car"]
n = 2
# n = 1


answer = []
temp = []


# for i in range(len(strings)):
    # temp.append([strings[i], strings[i][:n], strings[i][n:]])
    # temp[i] = strings[i][n:]

for i in strings:
    print(f'i[n] = {i[n]}')
    print(f'i[n]+i = {i[n]+i}')
    temp.append(i[n]+i)

# temp.sort(key = lambda answer : answer[0][n])
print(temp)
temp.sort()
print(temp)

'''
[
    ['abcd', 'ab', 'cd'],
    ['abce', 'ab', 'ce'],
    ['cdx', 'cd', 'x']
]
'''
# print(temp)

for i in temp:
    answer.append(i[1:])

print(answer)

# https://dydwnsekd.tistory.com/73
# https://codingpractices.tistory.com/57