'''소수 찾기'''

def solution(n):
    answer =0
    for i in range(2,n+1):
        j=1
        flag = True
        while j < i//2:
            j += 1
            if i%j==0:
                flag = False
                break
        if flag:
            answer +=1
    return answer