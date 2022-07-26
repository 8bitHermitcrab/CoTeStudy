# https://dev-note-97.tistory.com/89
# s.title() 이용 (hello -> Hello)

def solution(s):
    
    #첫 번째 문자 대문자로
    st = s.title()
    
    #띄어쓰기 단위로 쪼개서 맨 앞이 숫자인 경우 따로 하기
    w = st.split(" ")
    
    for i in range(len(w)):
        #단어 맨 앞에 숫자? -> .isdigit() -> 소문자로
        if len(w[i]) != 0 and w[i][0].isdigit():
            w[i] = w[i].lower()
    
    #합쳐서 출력        
    return " ".join(w)