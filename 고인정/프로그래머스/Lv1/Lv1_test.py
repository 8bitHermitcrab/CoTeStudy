# 모의고사

answers = [1, 3, 2, 4, 2]

def solution(answers):
    ans = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    sol = [0] * len(ans)
    
    for i, j in enumerate(answers):
        print(f'i j = {i, j}')
        for k, p in enumerate(ans):
            print(f'k p = {k, p}')
            if j == p[i % len(p)]:
                print(f'p[i % len(p)] = {p[i % len(p)]}')
                sol[k] += 1
    return [k + 1 for k, p in enumerate(sol) if p == max(sol)]

print(solution(answers))


    # https://zoeful-log.tistory.com/m/68