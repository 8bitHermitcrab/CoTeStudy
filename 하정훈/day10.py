### 서울에서 김서방 찾기 ###
# 문제 설명
# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요.
#  seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# 제한 사항
# seoul은 길이 1 이상, 1000 이하인 배열입니다.
# seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# "Kim"은 반드시 seoul 안에 포함되어 있습니다.

def solution(seoul):
    for index, name in enumerate(seoul):
        if name == "Kim":
            answer = "김서방은 "+str(index)+"에 있다" 
            return answer


# 다른 풀이

def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
    


### 문자열 다루기 기본 ###
# 문제 설명
# 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
# 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

# 제한 사항
# s는 길이 1 이상, 길이 8 이하인 문자열입니다.


def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
      return True

    else:
      return False



### 문자열 내림차순으로 배치하기 ###
# 문제 설명
# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

# 제한 사항
# str은 길이 1 이상인 문자열입니다.

# "Zbcdefg"	"gfedcbZ"

def solution(s):
    lst= []
    for i in s:
      lst.append(i)
      lst.sort()
      lst.reverse()
    return ''.join(lst)

# 다른 풀이

def solution(s):
    return ''.join(sorted(s, reverse=True))


### 문자열 내 p와 y의 개수 ###
# 문제 설명
# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다.
#  s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
# 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

# 예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.

# 제한사항
# 문자열 s의 길이 : 50 이하의 자연수
# 문자열 s는 알파벳으로만 이루어져 있습니다.
# 입출력 예
# s	answer
# "pPoooyY"	true
# "Pyy"	false
# 입출력 예 설명
# 입출력 예 #1
# 'p'의 개수 2개, 'y'의 개수 2개로 같으므로 true를 return 합니다.

# 입출력 예 #2
# 'p'의 개수 1개, 'y'의 개수 2개로 다르므로 false를 return 합니다.

# ※ 공지 - 2021년 8월 23일 테스트케이스가 추가되었습니다.

def solution(s):
    answer = True
    pCount = yCount = 0
    for i in range(len(s)):
        if s[i].lower()=='p':
            pCount += 1
        elif s[i].lower()=='y':
            yCount += 1
    if pCount != yCount:
        answer = False   
    
    return answer

# 다른 풀이

def solution(s):
    return s.lower().count('p') == s.lower().count('y')