# k진수에서 소수 개수 구하기

# n = 437674
# k = 3

n = 110011
k = 10

def solution(n, k):
    base = ''

    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)

    word = base[::-1].split('0')
    cnt = 0

    for w in word:
        if len(w) == 0:
            continue
        if int(w) < 2:
            continue
        
        prime = True
        for i in range(2, int(int(w)**0.5)+1):
            if int(w) % i == 0:
                prime = False
                break
        if prime:
            cnt += 1

    return cnt

print(solution(n, k))

# https://velog.io/@hope1213/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-k%EC%A7%84%EC%88%98%EC%97%90%EC%84%9C-%EC%86%8C%EC%88%98-%EA%B0%9C%EC%88%98-%EA%B5%AC%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

'''
def base(n, k):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    return rev_base[::-1]

# print(base(n, k))

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer_list = base(n, k).split('0')
    cnt = 0

    # print(answer_list)
    for i in answer_list:
        if i == '':
            pass
        else:
            i = int(i)
            # print(i)
            # if i > 1:
            if is_prime(i) == True:
                cnt += 1
                        
    return cnt
'''