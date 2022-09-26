# 카펫

brown = 10
yellow = 2

def solution(brown, yellow):
    answer = []
    # total = yellow + brown = width * height
    # yellow = (width - 2) * (height - 2)
    # brown = total - yellow

    total = yellow + brown
    
    # a * b = total
    for b in range(1, total+1):
        # total / b = a
        if (total / b) % 1 == 0:
            a = total // b
            if a >= b:
                # (a * 2) + (b * 2) = brown + 4
                if (a * 2) + (b * 2) == brown + 4:
                    return [a, b]

    return answer

print(solution(brown, yellow))

# https://dev-note-97.tistory.com/87