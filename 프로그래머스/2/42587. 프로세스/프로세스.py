from collections import deque
def solution(priorities, location):
    arr = deque()
    for i, v in enumerate(priorities):
        arr.append((v,i))
    cnt = 0
 
    while True:
        max_V = max(arr, key=lambda x: x[0])[0]
        now = arr.popleft()
        
        
        if max_V == now[0]:
            cnt += 1
            if now[1] == location:
                return cnt
        else:
            arr.append(now)
    return cnt