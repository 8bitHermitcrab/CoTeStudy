#https://eda-ai-lab.tistory.com/475

#완전탐색

#라이브러리 itertools: product(중복순열)
#https://blog.naver.com/hunii123/222346541826
#product: iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산
#단, product는 원소를 중복하여 뽑음
#객체를 초기화할 때는 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어줌 (기본값은 iterable 객체의 모든 원소 뽑아서 나열하기)
#product는 리스트 자료형으로 변환해서 사용한다

from itertools import product

def solution(numbers, target):
    
    #+, - 
    l = [(x, -x) for x in numbers]
    
    #print(l)
    #print(list(product(*l)))
    
    #모든 경우의 수 더하기
    s = list(map(sum, product(*l)))
    
    #print(s)
    
    
    #s 안에서 target의 갯수 세기
    return s.count(target)




#BFS
#DFS