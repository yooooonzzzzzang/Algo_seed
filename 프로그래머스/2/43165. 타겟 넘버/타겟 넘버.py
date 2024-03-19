def solution(numbers, target):
    
    
    def dfs(l, now):
        nonlocal answer
        if l == len(numbers):
            if now == target:
                answer += 1
        else:
            dfs(l+1, now + numbers[l])
            dfs(l+1, now - numbers[l])
    
    
    
    answer = 0
    dfs(0,0)
    return answer