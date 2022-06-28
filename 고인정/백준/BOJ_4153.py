# 직각삼각형

while True:
    # 삼각형 세 변 입력받기
    x = list(map(int, input().split()))
    # 최대 크기의 변
    max_x = max(x)

    if sum(x) == 0:
        break
    x.remove(max_x)

    # 피타고라스 정리 : x^2 + y^2 = z^2
    if (x[0]**2) + (x[1]**2) == (max_x**2):
        print('right')
    else:
        print('wrong')


'''
x, y, h = map(int, input().split())

if (x**2)+(y**2) == (h**2):
    print('right')
else:
    print('wrong')'''

# https://ooyoung.tistory.com/107