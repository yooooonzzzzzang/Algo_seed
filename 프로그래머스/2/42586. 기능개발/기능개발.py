from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    q = deque()
    for i in range(len(progresses)):
        q.append(math.ceil((100-progresses[i])/speeds[i]))
    now = q.popleft()
    cnt = 1 
    while q:
        if q[0] <= now:
            cnt+=1
            q.popleft()
        else:
            now = q.popleft()
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    return answer