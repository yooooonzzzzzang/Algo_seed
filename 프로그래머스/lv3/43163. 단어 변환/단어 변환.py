from collections import deque
def solution(begin, target, words):
    # 예제 2
    if target not in words:
        return 0

    q = deque()
    q.append((begin,0))

    while q:
        visited = [0]*len(words)
        word,idx = q.popleft()
        
        if word == target:
            return idx
        for i in range(len(words)):
            for j in range(len(words[i])):
                if word[j] == words[i][j]:
                    visited[i] +=1
        for i in range(len(visited)):
            if visited[i] == (len(begin)-1):
                q.append((words[i],idx+1))
                words[i] = str(idx)
    return 0