'''같은 숫자는 싫어'''

def solution(arr):
    answer = []
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:  #다음에 들어올 숫자와 같지 않을 경우에만 추가하기
            answer.append(arr[i])
    answer.append(arr[-1]) # 마지막 값만 따로 추가해주기
    return answer