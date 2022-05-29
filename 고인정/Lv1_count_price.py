# 부족한 금액 계산하기

price = 3
money = 20
count = 4


answer = 0

sum_price = price * count
for i in range(price, sum_price+1, price):
    money -= i
    if money < 0:
        answer = money * -1

print(answer)