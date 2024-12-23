n = int(input())
arr = list(input())
max_v = 0
for i in range(n):
    for j in range(i+1,n):
        if arr[i] == '1':
            if arr[j] =='1':
                if j-i > max_v:
                    max_v = j-i
                    max_idx = (i,j)
                break


max_v2 = -1
max_idx2 = 0
if arr[0] == '0':
    for i in range(n):
        if arr[i] == '1':
            max_v2 = i
            break
if arr[-1] == '0':
    for i in range(n-1,-1,-1):
        if arr[i] =='1':
            if max_v2 <= n-1-i:
                max_v2 = n-1-i
                max_idx2 = i
            break
if max_v2 >= max_v //2:
    arr[max_idx2] = '1'
else:
    arr[(max_idx[0] + max_idx[1]) // 2] = '1'

ans = 1000
for i in range(n):
    for j in range(i+1,n):
        if arr[i] == '1':
            if arr[j] =='1':
                if j-i < ans:
                    ans = j-i
                break
print(ans)
      



    