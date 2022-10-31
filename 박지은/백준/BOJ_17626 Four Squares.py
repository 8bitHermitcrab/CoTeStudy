#https://blog.naver.com/tladhehd/222852903697
#컴파일 에러
#모르겠어요...
n = int(input())

squares = [i*i for i in range(1, 224)]

for n in squares:
    print(1)
    exit()

for i in range(1, int(n**0.5)+1):
    for n-i*i in squares:
        print(2)
        exit()

for i in range(1, int(n**0.5)+1):
    for j in range(1, int(n**0.5)+1):
        if n-i*i-j*j in squares:
            print(3)
            exit()

print(4)
