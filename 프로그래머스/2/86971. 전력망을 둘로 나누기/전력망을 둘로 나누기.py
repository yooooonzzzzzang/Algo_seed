def solution(n, wires):
    answer =100000000
    arr = [[] for _ in range(n+1)] 
    
    for i in range(n-1):
        aa, bb = wires[i][0], wires[i][1]
        arr[aa].append(bb)
        arr[bb].append(aa)
        
    def dfs(node, v):
        global cnt
        v[node] = 1
        cnt += 1
        for i in arr[node]:
            if not v[i] :
                dfs(i, v)
                
        
    def cut(wire):
        global cnt
        v = [0] * (n+1)
        a,b = wires[wire][0], wires[wire][1]
        # 제거 
        arr[a].remove(b)
        arr[b].remove(a)
        # count 
        cnt = 0
        dfs(a, v)
        j = abs(n - cnt - cnt)
        
        arr[a].append(b)
        arr[b].append(a)
        return  j
    # 전력망 나누기
    for i in range(n-1):
        t = cut(i)
        if answer >= t:
            answer = t

    return answer