#https://blog.naver.com/jy8767/223032757942
import itertools
N = int(input())

#숫자들 리스트에 넣기
lst = [i for i in range(1, N+1)]

#숫자들 조합
#itertools.permutations(a, b) -> a에서 3개를 뽑아 조합을 만들어줌
#print(list(itertools.permutations([1,2,3], 3)))
arr = list(itertools.permutations(lst, N))

arr.sort()
for j in sorted(arr):
    print(*j)
