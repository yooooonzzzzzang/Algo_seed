
def solution(n, computers):
    visited = [0] * n
    answer = 0
    
    def dfs(v):
        visited[v] = 1
        for next_v in range(n): 
            if computers[v][next_v] ==1 and not visited[next_v]:
                dfs(next_v)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer +=1

    
    
    
    return answer

