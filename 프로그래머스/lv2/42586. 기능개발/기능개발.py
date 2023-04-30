import math
def solution(progresses, speeds):
    answer = []
    day = []
    
    for i in range(len(progresses)):
        day.append(math.ceil((100 - progresses[i])/speeds[i]))
    n = len(day)
    now = 0
    answer = []
    for i in range(1,n):
        if day[i] > day[now]:
            answer.append(i - now)
            now = i
    answer.append(n-now)
    
    return answer