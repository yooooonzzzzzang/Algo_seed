K, N = map(int, input().split())

# Write your code here!
strs = ""
def recur():
    global strs
    if len(strs) == N:
        print(*strs)
        return 
    for i in range(1,K+1):
        strs += str(i)
        recur()
        strs = strs[:-1]
recur()