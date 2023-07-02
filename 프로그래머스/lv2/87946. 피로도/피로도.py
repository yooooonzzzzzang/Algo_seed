answer  =0 
def dfs(k,visited, dungeons, cnt):
    global answer
    answer = max(answer, cnt)
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i]  = 1
            dfs(k-dungeons[i][1],visited, dungeons, cnt+1)
            visited[i] = 0


def solution(k, dungeons):
    visited = [0] * len(dungeons)

    dfs(k,visited, dungeons, 0)

    return answer