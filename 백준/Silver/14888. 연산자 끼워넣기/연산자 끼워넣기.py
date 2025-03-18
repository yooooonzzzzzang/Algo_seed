N = int(input())
arr = list(map(int,input().split()))
add, sub, mul, div = list(map(int,input().split()))
mn, mx = int(1e9), int(-1e9)
def recur(n, sm, add, sub, mul, div):
    global mn, mx
    if int(-1e9) > sm or int(1e9) <sm:
        return
    if n == N:
        mx = max(mx, sm)
        mn = min(mn, sm)
        return 
    if add >0:
        recur(n+1, sm+arr[n], add -1 , sub, mul, div)
    if sub >0:
        recur(n+1, sm-arr[n], add , sub-1, mul, div)
    if mul >0:
        recur(n+1, sm*arr[n], add , sub, mul-1, div)
    if div >0:
        recur(n+1, int(sm/arr[n]), add , sub, mul, div-1)

recur(1, arr[0], add, sub, mul, div)
print(mx, mn, sep='\n')
