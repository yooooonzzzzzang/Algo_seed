def solution(n, computers):
    answer = 0
    v = [0] * n
    
    def dfs(node):
        v[node] = 1
        for i in range(n):
            if computers[node][i] == 1 and not v[i]:
                dfs(i)
    
    for i in range(n):
        if not v[i]:
            dfs(i)
            answer+=1
    return answer