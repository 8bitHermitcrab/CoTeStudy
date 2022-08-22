# 달팽이는 올라가고 싶다

import math

a, b, v = map(int, input().split())

# An - B(n-1) = V
day_count = (v-b)/(a-b)
print(day_count)
print(math.ceil(day_count))