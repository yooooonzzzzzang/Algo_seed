n = int(input())
arr = list(map(int,input()))
ans = 0 
def solution():
    ans = 10000
    now = arr.index(1)
    for i in range(now+1,n):
        if arr[i] == 1:
            ans = min(ans, i-now)
            now = i
    return ans
for i in range(n):
    for j in range(n):
        if not arr[i] and not arr[j]:
            arr[i] = 1 
            arr[j] = 1
            
            ans = max(ans, solution())
            
            # 원복 
            arr[i] = 0
            arr[j] = 0
print(ans)