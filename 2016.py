'''2016년, a월 b일에 해당하는 요일 출력하기'''

def solution(a, b):
    day = ['FRI', 'SAT','SUN','MON','TUE','WED','THU']  #요일 입력
    date = {1:31, 2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}  # 딕셔너리를 사용해서 월에 해당하는 일 value 입력
    num =0
    for i in range(1,a): # a-1까지 일을 더하기
        num += date.get(i)
    num = (num+b) % 7  # b만큼 더한 후 7로 나누기
    return day[num-1]  # 나머지에 해당하는 값 출력하기
