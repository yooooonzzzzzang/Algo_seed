n = int(input())
arr = input().split()
for i in range(n):
    arr[i] = [int(arr[i]), i]
sorted_arr = sorted(arr, key=lambda x:x[0])
for i in range(n):
    if i!=0 :
        if sorted_arr[i][0] == sorted_arr[i-1][0]:
            sorted_arr[i] = [*sorted_arr[i], sorted_arr[i-1][2]]
        else:
            sorted_arr[i] = [*sorted_arr[i], sorted_arr[i - 1][2]+1]
    else: sorted_arr[i] = [*sorted_arr[i], i]
sorted_arr.sort(key=lambda x:x[1])
for a,b,c in sorted_arr:
    print(c, end=" ")


'''

-10 2 0
-9 4 1
2 0 2
4 1 3
4  3 4
'''






