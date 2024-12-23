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
print(max_v)