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

arr[(max_idx[1] + max_idx[0])//2] = '1'
max_v = 1000
for i in range(n):
    for j in range(i+1,n):
        if arr[i] == '1':
            if arr[j] =='1':
                if j-i < max_v:
                    max_v = j-i
                break


arr[(max_idx[1] + max_idx[0])//2] = '0'

for i in range(1,n):
    if arr[i] == '1' and arr[0] =='0':
        max_v = max(max_v, i)
        break
for i in range(n-2, -1,-1):
    if arr[i] == '1' and arr[-1] =='0':
        max_v = max(max_v, n-1-i)
        break
print(max_v)
