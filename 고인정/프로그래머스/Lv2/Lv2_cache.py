# [1차] 캐시

# 25
# cacheSize = 0
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

# 50
cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

def solution(cacheSize, cities):
    # 실행시간
    answer = 0
    cache = []

    for i in cities:
        i = i.lower()
        if cacheSize != 0:
            if not i in cache:
                if len(cache) == cacheSize:
                    cache.pop(0)
                cache.append(i)
                answer += 5
            else:
                # print(cache.index(i))
                cache.pop(cache.index(i))
                cache.append(i)
                answer += 1
            print(cache)
            print(f'cache.index({i}) = {cache.index(i)}')
        else:
            answer += 5
    
    return answer

print(solution(cacheSize, cities))

# https://velog.io/@tiiranocode/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%BA%90%EC%8B%9C


'''
def solution(cacheSize, cities):
    # 실행시간
    answer = 0
    cache = []
    # LRU (Least Recently Used)
    
    # 캐시 허용 크기보다 작을 때(캐시에 그대로 저장될 수 있음)
    # 캐시 허용 크기보다 같거나 클 때(최근에 사용되지 않은 걸 빼야함)
    
    for i in cities:
        # print(f'i = {i}')
        i = i.lower()
        # 캐시 안에 있을 때
        if i in cache:
            # cache.append(i)
            answer += 1
            # print(f'cache_in = {cache}')
        # 캐시 안에 없을 때
        else: 
            if cacheSize == 0:
                answer += 5
            else:    
                if len(cache) == cacheSize:
                    del cache[0]
                    # cache.pop(0)
                cache.append(i)
                answer += 5
                # print(f'cache_not = {cache}')

    # print(f'cache = {cache}')
    
    return answer

print(solution(cacheSize, cities))
'''