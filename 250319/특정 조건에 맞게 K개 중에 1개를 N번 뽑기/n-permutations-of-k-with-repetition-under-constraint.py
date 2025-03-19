K, N = map(int, input().split())

# Please write your code here.

arr =[]
def recur(n):
    if n==N:
        print(*arr)
        return 
    for i in range(1,K+1):
        # if len(arr) < 3 or i != arr[-2]:
        if len(arr) < 2 or not (arr[-1] == arr[-2] == i):
            arr.append(i)
            recur(n+1)  
            arr.pop()
recur(0)