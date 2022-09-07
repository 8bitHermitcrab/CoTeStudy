# 비밀번호 찾기

n, m = map(int, input().split())

password_dict = dict()

for i in range(n):
    site, password = input().split()
    password_dict[site] = password

for i in range(m):
    q_site = input()
    print(password_dict[q_site])