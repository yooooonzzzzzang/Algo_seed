from collections import deque
def solution(begin, target, words):
    answer = 0
    v = [0] * len(words)
    q = deque()
    q.append((begin,0))
    
    while q:
        w, cnt = q.popleft()
        if w == target:
            return cnt
        for i in range(len(words)):
            w_cnt = 0
            if not v[i]:
                for j in range(len(words[i])):
                    if words[i][j] == w[j]:
                        w_cnt+=1
                if w_cnt + 1 == len(words[i]):
                    q.append((words[i], cnt+1))
                    v[i] = 1

    return answer