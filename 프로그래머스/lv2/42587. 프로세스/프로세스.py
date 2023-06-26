from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for i, x in enumerate(priorities):
        q.append((i,x))
        
        
    while True:
        now = q.popleft()
        if any(now[1] < qu[1] for qu in q):
            q.append(now)
        else:
            answer += 1
            if location == now[0]:
                return answer
        
