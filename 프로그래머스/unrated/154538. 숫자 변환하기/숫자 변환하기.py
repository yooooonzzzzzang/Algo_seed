from collections import deque
def solution(x, y, n):
    q = deque()
    answer = 0
    v = [0] * 1000001 
    q.append((x, 0))
    v[x] = 1
    while q:
        new_x, cnt = q.popleft()
        if new_x == y:
            return cnt
        for dir in (new_x+n, new_x*2, new_x*3):
            if 0<=dir<=y  and not v[dir]:
                v[dir] = 1
                q.append((dir, cnt+1))
    return -1