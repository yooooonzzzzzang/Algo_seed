def solution(s):
    answer = ''
    arr = list(map(int, s.split(" ")))
    return str(min(arr)) + " " + str(max(arr))