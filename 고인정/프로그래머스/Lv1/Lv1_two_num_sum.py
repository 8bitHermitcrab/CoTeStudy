# 두 개 뽑아서 더하기


# numbers = [2,1,3,4,1]
numbers = [5,0,2,7]

# 결과 중복 제거
answer = set()

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        answer.add(numbers[i] + numbers[j])

answer = list(answer)
answer.sort()


###

answer = []
temp = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        v = numbers[i] + numbers[j]
        answer.append(v)
    w = numbers[i] + numbers[i]
    answer.remove(w)

print(answer)        
answer = list(set(answer))
print(answer)
answer.sort()
print(answer)

# https://velog.io/@ckr3453/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%91%90-%EA%B0%9C-%EB%BD%91%EC%95%84%EC%84%9C-%EB%8D%94%ED%95%98%EA%B8%B0



'''

# 우리의 생각
# [2,1,3,4,1] 첫번째 원소 2뽑아
# [1,3,4,1] 첫번째 원소 1뽑아
# [3,4,1] 첫번째 원소 3뽑아
# [4,1] 첫번째 원소 4뽑아
# [1] 첫번째 원소 1뽑아

# 컴퓨터 하는 방식
# [2,1,3,4,1] 첫번째 원소 2뽑아
# [1,3,4,1] 두번째 원소 3뽑아
# [1,4,1] 세번째 원소 1뽑아
# [1,4] 네번째원소가 없네? 종료

remove 사용시 원본 데이터 훼손으로 누락 발생
https://devpouch.tistory.com/110

sorted는 다른 리스트로 재정의됨
https://www.codeit.kr/community/threads/186

'''