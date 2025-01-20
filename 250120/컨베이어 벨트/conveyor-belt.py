n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Write your code here!
# t초만큼 
for i in range(t):
    tmp = [u[-1]]
    # u 배열을 오른쪽으로 옮겨주고
    for i in range(n-1,0,-1):
        u[i] = u[i-1] 
    # d 배열을 왼쪽으로 옮겨준다
    u[0] = d[n-1]
    for i in range(n-1,0,-1):
        d[i] = d[i-1] 
    d[0] = tmp[0]
print(*u)
print(*d)