#import sys
#input = sys.stdin.readline

N = int(input())
nums = []

for _ in range(N):
    nums.append(int(input()))

#계단 마지막은 반드시 밞아야 하니까
answer = nums[-1]
print(answer)