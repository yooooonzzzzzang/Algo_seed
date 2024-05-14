for _ in range(int(input())):
    n = int(input())
    arr = [[0]+list(map(int, input().split())) for _ in range(2)]
    ans = 0
    if n == 1:
        ans = max(arr[0][1], arr[1][1])
        print(ans)
        continue
    elif n== 2:
        ans = max(arr[0][2] + arr[1][1] , arr[0][1] + arr[1][2])
        print(ans)
        continue
    else:
        for i in range(1,n):
            arr[0][i+1] =  max(arr[1][i],arr[1][i-1]) + arr[0][i+1]
            arr[1][i+1] =  max(arr[0][i],arr[0][i-1]) + arr[1][i+1]
        # print(arr)
        print(max(arr[0][n], arr[1][n]))
        continue
        
