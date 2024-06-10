n = int(input())
answer = 0
v1 = [0] * n
v2 = [0] * (2*n)
v3 = [0] * (2*n)
    
def dfs(x):
    global answer
    if x == n:
        answer += 1
        return
    for i in range(n):
        if v1[i] == v2[x+i] == v3[x-i] == 0:
            v1[i] = v2[x+i] = v3[x-i] = 1
            dfs(x+1)
            v1[i] = v2[x+i] = v3[x-i] = 0
    
dfs(0)
print(answer)
