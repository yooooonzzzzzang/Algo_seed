import math
def solution(n, stations, w):
    answer = 0
    erea = []
    for i in stations:
        st = i-w
        ed = i+w
        if st < 0:
            st = 0
        if ed > n:
            ed = n
        erea.append([st,ed])

    empty = []
    start = 1
    for s,e in erea:
        if start < s:
            empty.append([start, s-1])
        start = e + 1
    if start <= n:
        empty.append([start,n])
    
    for s,e in empty:
        answer += math.ceil((e-s+1)/(2*w + 1))
    return answer