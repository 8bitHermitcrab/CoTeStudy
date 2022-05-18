# 시저 암호

# s = "a B z"
s = 'z'
# s = 'AB'
n = 25

alpabet = 'abcdefghijklmnopqrstuvwxyz'

# print(ord('a')) # 97
# print(ord('A')) # 65
# print(ord('z')) # 122
# print(ord('Z')) # 90
# print(chr(65))
# print(ord(' ')) # 32
# print(chr(96 + n))
answer = ''

print(answer)

'''
for i in range(len(s)):
    # 아스키 코드로 바꾸기
    ord_s = ord(s[i])
    if ord_s != 32: # 공백이 아닐 때
        if ord_s == 90: # Z일 때
            ord_spn = 64 + n
            chr_spn = chr(ord_spn)
        elif ord_s == 122: # z일 때
            ord_spn = 96 + n
            if ord_spn > 122:
                n = ord_spn - 122
                ord_spn = 64 + n
                chr_spn = chr(ord_spn)
            else:
                ord_spn = 96 + n
                chr_spn = chr(ord_spn)
        else:
            # 아스키 코드에 +n
            ord_spn = ord_s + n
            # 아스키 코드를 다시 문자로 변환
            chr_spn = chr(ord_spn)
    else:
        chr_spn = chr(32)
    answer = answer + chr_spn
'''