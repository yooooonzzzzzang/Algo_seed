n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt1 = 0
cnt2 = 0
for i in range(n):
    if arr[i][0] < arr[i][1]:
        cnt1 +=1
    elif arr[i][0] > arr[i][1]:
        cnt2 += 1
print(max(cnt1, cnt2))