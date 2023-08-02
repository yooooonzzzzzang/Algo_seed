def solution(a, b):
    # 윤년 29일
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    # 인덱스1에 금요일이 오도록
    days= ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    return days[(sum(months[:a-1])+b)%7]