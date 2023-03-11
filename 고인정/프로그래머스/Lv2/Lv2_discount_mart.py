# 할인 행사

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]


from collections import Counter

def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]): 
            answer += 1
    return answer


print(solution(want, number, discount))

# https://velog.io/@dlrjs2360/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Python3-%ED%95%A0%EC%9D%B8-%ED%96%89%EC%82%AC

'''

def solution(want, number, discount):
    answer = 0
    
    want_dict = dict()
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    discount_dict = dict()
    for i in discount:
        try:
            discount_dict[i] = 1
        except:
            discount_dict[i] += 1

    print(want_dict)
    # print(discount_dict)
    
    print(discount_dict.keys())
    
    for key, value in want_dict.items():
        if key in discount_dict.keys():
            answer += 1
        
    return answer

'''