'''콜라츠 추측'''

def solution(num):
    i = 0
    while i != 500:
        if num ==1: return i
        elif num %2 ==0: num //= 2
        else: num = num *3 +1
        i+=1
    return -1