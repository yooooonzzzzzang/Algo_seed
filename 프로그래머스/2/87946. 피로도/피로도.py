def solution(k, dungeons):
    answer = -1

    
    def dfs(now, l, cnt):
        nonlocal answer 
        answer = max(answer, cnt)

        for i in range(len(dungeons)):
            if not v[i] and now >= dungeons[i][0]:
                v[i] = 1
                dfs(now-dungeons[i][1], l+1, cnt+1)
                v[i] = 0
    v = [0] * len(dungeons)
    dfs(k,0,0)
    return answer