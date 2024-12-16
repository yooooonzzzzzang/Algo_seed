n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

flag = "Yes"
# 제외할 선분
for k in range(n):

    for i in range(k+1, n):
 
        for j in range(k+2, n):
            x1, x2 = arr[i][0], arr[i][1]
            x3, x4 = arr[j][0], arr[j][1]
            # 안겹치면 No
            if x2 < x3 or x4 < x1:
                flag = "No"


print(flag)