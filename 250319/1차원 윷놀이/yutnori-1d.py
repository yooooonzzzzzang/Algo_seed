N, M, K = map(int, input().split())
nums = list(map(int, input().split()))
arr =[]
# Please write your code here.

maps = [0] * M
ans = 0
def cal(arr):
    position = [1 for _ in range(K)]
    for i in range(N):
        position[arr[i]-1] += nums[i]
    cnt = 0
    for p in position:
        if p >= M:
            cnt +=1 
    return cnt 

def recur(n):
    global ans 
    if n == N:
        ans = max(ans, cal(arr))
        return
    for i in range(1,K+1):
        arr.append(i)
        recur(n+1)
        arr.pop()
recur(0)
print(ans)