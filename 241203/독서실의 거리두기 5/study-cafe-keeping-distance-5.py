n = int(input())
arr = list(map(int,input()))

ans = []
for i in range(n):
    max_ans = 21
    if arr[i] == 0:
        arr[i] = 1
        
        index_i = []
        
        for j in range(n):
            if arr[j] == 1:
                index_i.append(j)
        for j in range(1,len(index_i)):
            max_ans = min(index_i[j] - index_i[j-1], max_ans)
        
        ans.append(max_ans)
        arr[i] = 0
print(max(ans))