N = int(input())
num = list(map(int, input().split()))
ans = 10
# Please write your code here.
def recur(n,cnt):
    global ans
    if n >= N-1:
        ans = min(ans, cnt)
        return
    for i in range(1,num[n]+1):
        recur(n+i, cnt+1)
recur(0,0)
print(ans if ans != 10 else -1)