# 할인 행사

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

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

print(solution(want, number, discount))