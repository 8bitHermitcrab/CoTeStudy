# 집합

# add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다. 

import sys

s = set()

# 연산 수
m = int(sys.stdin.readline())

for i in range(m):
    order = sys.stdin.readline().strip().split()

    if len(order) == 1:
        if order[0] == 'all':
            s = set([j for j in range(1, 21)])
        else:
            s = set()

    else:
        cmd, num = order[0], int(order[1])

        if cmd == 'add':
            s.add(num)
        elif cmd == 'check':
            print(1 if num in s else 0)
        elif cmd == 'remove':
            # remove는 keyError 발생o, discard는 keyError 발생x
            if num in s:
                s.discard(num)
        elif cmd == 'toggle':
            if num in s:
                s.discard(num)
            else:
                s.add(num)

# https://begin-dev-awos.tistory.com/163

'''

import sys

s = set()

# 연산 수
m = int(sys.stdin.readline())

# order = []
for i in range(m):
    order = sys.stdin.readline().strip().split()

    if len(order) == 1:
        if order[0] == 'all':
            s = set([j for j in range(1, 21)])
        else:
            s = set()
        continue

command, num = order[0], order[1]
num = int(num)

if command == 'add':
    s.add(num)
elif command == 'check':
    print(1 if num in s else 0)
elif command == 'remove':
    # remove는 keyError 발생o, discard는 keyError 발생x
    s.discard(num)
elif command == 'toggle':
    if num in s:
        s.discard(num)
    else:
        s.add(num)

print(order)
print(s)
'''

# https://mong9data.tistory.com/91

# https://www.delftstack.com/ko/howto/python/python-remove-element-from-set/

# for i in order:
    # if order[:3] == 'add':
    #     if order[-1] in s:
    #         pass
    #     else:
    #         s.add(order[1])
    # # remove
    # elif order[:3] == 'rem':
    #     if order[-1] in s:
    #         pass
    #     else:
    #         s.remove(order[-1])
    # # check
    # elif order[:3] == 'che':
    #     if order[-1] in s:
    #         print(1)
    #     else:
    #         print(0)
    # # toggle
    # elif order[:3] == 'tog':
    #     if order[-1] in s:
    #         s.remove(order[-1])
    #     else:
    #         s.add(order[-1])
    # elif order[:3] == 'all':
    #     s.update([j for j in range(1, 21)])
    # # empty
    # elif order[:3] == 'emp':
    #     s = set()

# https://wikidocs.net/1015