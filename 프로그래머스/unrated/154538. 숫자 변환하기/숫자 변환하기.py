from collections import deque
def solution(x, y, n):
    q = deque()
    answer = 0
    v = [0] * 1000001
    # bfs 이용해서 y 보다 커지면 이전으로 돌아가서 다르게 하고 싶음 y 랑 같으면 stop 
    q.append((x, 0))
    v[x] = 1
    while q:
        x, cnt = q.popleft()
        if x == y:
            return cnt
        for dir in (x+n, x*2, x*3):
            if 0<=dir<= 1000000 and not v[dir]:
                v[dir] = 1
                q.append((dir, cnt+1))
    return -1