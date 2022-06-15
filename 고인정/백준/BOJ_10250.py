# ACM 호텔

t = int(input())
hotel = []
answer = []

for i in range(t):
    # h: 층 수, w: 각 층의 방 수, n: n번째 손님
    h, w, n = map(int, input().split())
    # hotel.append([h, w, n])
# print(hotel)
    # 층수 h는 n % h
# 호수는 
# print(10 % 6) # 4
# print(10 // 6) # 1
# print(72 % 30) # 12
# print(72 // 30) # 2

    # abb호 또는 aabb호
    a = n % h
    b = (n // h) + 1

    # str_X = str(X)
    # str_w = str(w)
    # # 호수 자리수 맞추기
    # if len(str_X) < len(str_w):
    #     XX = str_X.zfill(len(str_w))
    
    # YYXX = str(Y) + XX
    # answer.append(int(YYXX))

    # 층수 5%5 = 0층
    # 룸번호 5/5 + 1 = 2호
    # 002
    if a == 0:
        a = h
        b -= 1
    print(a*100 + b)

'''
# t개의 테스트 
t = int(input())
# h : 호텔의 층수, w : 각 층의 방수, n : n번째 손님
for _ in range(t):
    h, w, n = map(int, input().split())
    a = n % h
    b = n // h+1
    if a == 0:
       a = h
       b -= 1
    print(a*100 +b)
'''