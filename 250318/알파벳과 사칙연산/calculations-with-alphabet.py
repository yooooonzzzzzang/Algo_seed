expression = input()
N = len(expression)
ol = N//2 
nl = N-ol
def cal(tmp):
    global ans
    val = tmp[0]
    for i in range(1, nl):
        if val <  -int(1e9) or val > int(1e9):
            return
        operator = expression[2*i-1]
        if operator == '+':
            val += tmp[i] 
        if operator == '*':
            val *= tmp[i] 
        if operator == '-':
            val -= tmp[i] 

    ans = max(ans, val)
def recur(n):
    if nl == n:
        cal(arr)
        return
    for i in range(1,5):
        arr.append(i)
        recur(n+1)
        arr.pop()
arr = []
ans = -int(1e9)
recur(0)
print(ans)
# Please write your code here.
