# 최솟값 만들기

def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse = True)
    
    for i in range(len(A)):
        answer += (A[i] * B[i])
    
    return answer


# https://velog.io/@ssongplay/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%B5%9C%EC%86%9F%EA%B0%92-%EB%A7%8C%EB%93%A4%EA%B8%B0-Python