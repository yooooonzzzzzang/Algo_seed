from collections import deque
def solution(s):
    answer = []
    q = deque()
    for i in range(len(s)):
        for j in range(i,0,-1):
            if s[i] == s[j-1]:
                answer.append(i-(j-1))
                break
        else:
            answer.append(-1)
    return answer