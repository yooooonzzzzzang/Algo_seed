def solution(a, b):
    answer = ''
    # 윤년 2월이 29일까지 있음
    # 1월 1일 금요일이라 7로 나뉘면 인덱스 1이 금요일이 되도록 배열
    day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    mon = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
    
    return day[(sum(mon[:a-1])+b ) % 7]