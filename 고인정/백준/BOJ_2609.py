# 최대공약수와 최소공배수

a, b = map(int, input().split())


def gcd(a, b):
    if a%b == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

'''# 최대공약수
for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

# 최소공배수
for i in range(max(a, b), (a*b)+1):
    if i % a == 0 and i % b == 0:
        print(i)
        break'''