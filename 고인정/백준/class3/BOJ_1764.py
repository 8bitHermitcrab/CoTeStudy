# 듣보잡

n, m = map(int, input().split())

listen = {input() for _ in range(n)}
look = {input() for _ in range(m)}

print(f'listen = {listen}')
print(f'look = {look}')

answer = sorted(listen & look)
print(answer)
print(len(answer))

for i in answer:
    print(i)

# for i in listen:
#     for j in look:
#         if i == j:
#             print(j)