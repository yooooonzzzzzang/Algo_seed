'''
Step 0. 초기 위치
1 0 1 0 1 0 0 0 0 0 1

Step 1. 가장 먼 1 간의 쌍 찾기 (Y로 표기)
1 0 1 0 Y 0 0 0 0 0 Y

Step 2. 해당 쌍 가운데에 1 놓기
1 0 1 0 1 0 0 1 0 0 1

Step 3. 다시 가장 먼 1간의 쌍 찾기 (Z로 표기)
1 0 1 0 Z 0 0 Z 0 0 1

Step 4. Z간의 간격이 답 → 3

'''
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