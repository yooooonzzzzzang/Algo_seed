from collections import deque
def solution(n, m, section):
    answer = 1
    section = deque(section)
    # m: 롤러의 길이, n: 벽의 길의, section[]: 페인트 칠이 필요한 곳
    position = section[0]
    section.popleft()
    idx = 0 
    while section:
        paint = position+m-1
        if paint >= section[0]:
            section.popleft()
            
        else:
            answer += 1 
            position = section.popleft()
    return answer