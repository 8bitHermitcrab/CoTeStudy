# 숫자 문자열과 영단어


s = "one4seveneight"

def solution(s):
    numbers = {
                '0' : 'zero',
                '1' :'one',
                '2' : 'two',
                '3' : 'three',
                '4' : 'four',
                '5' : 'five',
                '6' : 'six',
                '7' : 'seven',
                '8' : 'eight',
                '9' : 'nine'
                }

    for key, value in numbers.items():
        s = s.replace(value, key)
    
    
    return int(s)


print(solution(s))