# 직사각형에서 탈출

x, y, w, h = map(int, input().split())


# ---------(w,h)
#      |    |
#----(x,y)--|
#      |    |
#      |    |
#############

# answer = list((((w-x)**2) + ((h-y)**2))**(1/2))
answer = min([x, y, w-x, h-y])
print(answer)

# https://ooyoung.tistory.com/102