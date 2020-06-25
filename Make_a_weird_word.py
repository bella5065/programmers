'''이상한 문자 만들기'''

def solution(s):
    answer = ''
    j=0
    for i in s:
        if i == ' ':
            answer += i
            j = -1
        elif j % 2==0:
            answer += i.upper()
        else:
            answer += i.lower()
        j +=1
    return answer