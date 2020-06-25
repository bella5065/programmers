'''가운데 글자 가져오기'''

def solution(s):
    if len(s) % 2 != 0:  # 글자의 개수가 홀수일 경우
        return s[len(s)//2]  # 2로 나눈 몫을 인덱스로 글자 출력
    else:
        return s[len(s)//2-1] + s[len(s)//2]  # 짝수일 경우 가운데 글자 2개 출력