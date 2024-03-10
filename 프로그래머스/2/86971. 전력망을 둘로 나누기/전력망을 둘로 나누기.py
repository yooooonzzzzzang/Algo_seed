def solution(n, wires):
    answer =100000000
    arr = [[] for _ in range(n+1)] 
    
    for i in range(n-1):
        aa, bb = wires[i][0], wires[i][1]
        arr[aa].append(bb)
        arr[bb].append(aa)
        
    def dfs(node, v):
        v[node] = 1
        cnt = 1
        for i in arr[node]:
            if not v[i] and i not in ():
                cnt += dfs(i, v)
        return cnt
                
        
    def cut(wire):
        v = [0] * (n+1)
        a,b = wires[wire][0], wires[wire][1]
        # 제거 
        arr[a].remove(b)
        arr[b].remove(a)
        # count 
        cnt = abs(dfs(a, v)-dfs(b, v))
        
        arr[a].append(b)
        arr[b].append(a)
        return  cnt
    # 전력망 나누기
    for i in range(n-1):
        t = cut(i)
        if answer >= t:
            answer = t
    # for i in range(n):
    #     cut(i)
        
        # if answer >= counting_cnt:
        #     answer = counting_cnt
    
    
    

    
#     for i in range(n):
#         v = [0] * (n+1)
#         tmp = cut(i)
#         if answer >= tmp:
#             answer= tmp

    return answer