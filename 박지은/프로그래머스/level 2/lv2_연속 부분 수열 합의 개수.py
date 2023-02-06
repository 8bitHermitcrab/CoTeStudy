#https://blog.naver.com/xkr1357/222943446852
def solution(elements):
    answer = 0
    #중복값 제거를 위해
    sum_lst = set()
    
    elements_2 = elements*2
    
    for i in range(len(elements)):
        for j in range(len(elements)):
            sum_lst.add(sum(elements_2[i:i+j+1]))
    
    answer = len(sum_lst)

    return answer