# 위장

# clothes = [의상의 이름, 의상의 종류]
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]

# 최소 1개 의상은 입는다.
# 의상은 1개 이상 30개 이하

def solution(clothes):

    # 옷 종류별로 구분하기
    hash = dict()
    for names, types in clothes:
        hash[types] = hash.get(types, 0) + 1
    print(hash)

    # 입지 않은 경우를 추가하여 모든 조합 계산하기
    answer = 1
    for types in hash:
        answer *= (hash[types] + 1)

    # 아무 종류도 입지 않은 경우 제외
    return answer-1

print(solution(clothes))


# 딕셔너리 get(x, '디폴트 값') 함수
# https://johnyejin.tistory.com/138

# https://coding-grandpa.tistory.com/88


'''
answer = 0
    
    for r, row in enumerate(clothes):
        for name, type in enumerate(row):
            print(r, name, type)
            answer += 1

    return answer-1
'''



'''
    hash = dict()
    for i in range(len(clothes)):
        try:
            hash[clothes[i][1]].append(clothes[i][0])
        except:
            hash[clothes[i][1]] = [clothes[i][0]]
    print(f'hash = {hash}')
    print(len(hash.keys()))
    print(len(hash.values()))

    types = 0
    camo = []
    for key, value in hash.items():
        types += 1
        print(types, key, value)
        # print(f'len(value) = {len(value)}')
        # answer += len(value)
        for j in value:
            camo.append(j)
        
        print(types, j)

    
    if types != 1:
        answer = types + answer
'''