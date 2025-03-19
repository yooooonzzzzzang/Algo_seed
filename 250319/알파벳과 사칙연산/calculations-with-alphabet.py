import sys
ans = -sys.maxsize
expressions = input()
num = [0] * 6

def convert(charac):
    return num[ord(charac) - ord('a')]

def cal():
    val = convert(expressions[0])
    for i in range(1,len(expressions),2):
        if expressions[i] == '+':
            val += convert(expressions[i+1])
        elif expressions[i] == '*':
            val *= convert(expressions[i+1])
        elif expressions[i] == '-':
            val -= convert(expressions[i+1])
    return val

def recur(n):
    global ans
    if n == 6:
        ans = max(ans, cal())
        return
    for i in range(1, 5):
        num[n] = i
        recur(n+1)
recur(0)
print(ans)