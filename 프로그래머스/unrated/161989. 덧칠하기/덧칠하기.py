from collections import deque 
def solution(n, m, section):
    dq=deque(section)
    cnt=1
    # 벽을 칠함
    roller=section[0]+m-1
    
    while dq:
        # flag보다 작으면 dq.pop()
        if dq[0]<=roller:
            dq.popleft()
        #아닐경우 flag 재지정
        else:
            cnt+=1
            roller=dq[0]+m-1
    return cnt