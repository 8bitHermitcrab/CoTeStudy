# 숫자 카드 2

# 숫자 카드 2

from sys import stdin

# 가지고 있는 숫자 카드의 개수 n
n = stdin.readline().rstrip()
cards = list(map(int, stdin.readline().split()))

# 가지고 있는 숫자 카드인지 구해야할 개수 m
m = stdin.readline().rstrip()
nums = list(map(int, stdin.readline().split()))

cnt = {}

for i in cards:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in nums:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')



'''
import sys

INPUT = sys.stdin.readline()

# 가지고 있는 숫자 카드의 개수 n
n = int(INPUT)

from sys import stdin

n = stdin.readline().rstrip()

cards = sorted(list(map(int, INPUT.split())))

# 가지고 있는 숫자 카드인지 구해야할 개수 m
m = int(INPUT)

nums = list(map(int, INPUT.split()))

print(cards)
print(nums)

for i in nums:
    print(cards.count(i), end=' ')

cnt = dict()
for i in cards:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for i in nums:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')


def BinarySearch(arr, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if arr[mid] == target:
        return cnt.get(target)
    elif arr[mid] < target:
        return BinarySearch(arr, target, mid+1, end)
    else:
        return BinarySearch(arr, target, start, mid-1)

for target in nums:
    print(BinarySearch(cards, target, 0, len(cards)-1), end=' ')

'''

# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10816-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%88%AB%EC%9E%90-%EC%B9%B4%EB%93%9C-2-%EC%8B%A4%EB%B2%844-%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89

# https://hongcoding.tistory.com/12