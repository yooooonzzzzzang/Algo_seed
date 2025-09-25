n = int(input())
arr = []
for _ in range(n):
    s, w = map(int, input().split())
    arr.append([s,w])

    # 내구도는 상대 계란의 무게만큼 깎이게 된다. 
    # 내구도가 0 이하가 되는 순간 계란은 깨지게 된다. 
ans  = 0
def dfs(x, cnt):
    global ans
    # 끝까지 가도 정답 x
    if ans >= (cnt + (n-x)*2): 
        return
    if x == n:
        ans = max(ans, cnt)
        return
    else:
# 손에 든계란 깨지면 다음으로
        if arr[x][0] <= 0:
            dfs(x+1, cnt)
        else:        
            flag = False
            for i in range(n):
                if i == x or arr[i][0] <= 0: 
                    continue
                flag = True
                arr[x][0] -= arr[i][1]
                arr[i][0] -= arr[x][1]
   
                dfs(x+1, cnt+int(arr[x][0]<=0)+int(arr[i][0]<=0))
                # 원상복구
                arr[x][0] += arr[i][1]
                arr[i][0] += arr[x][1]
            # 
            if flag == False:
                dfs(x+1, cnt)


dfs(0, 0)
print(ans)