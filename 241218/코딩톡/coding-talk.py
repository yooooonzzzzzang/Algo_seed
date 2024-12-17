n,m,p = map(int,input().split())
info = [input().split() for _ in range(m)]
alp = [chr(ord('A')+i) for i in range(n)]
for i in range(p-1,n):
    if info[i][0] in alp:
        alp.remove(info[i][0])
if info[p-1][1] != '0':
    print(*alp)
    