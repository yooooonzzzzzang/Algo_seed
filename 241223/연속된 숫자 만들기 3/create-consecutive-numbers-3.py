a,b,c = map(int,input().split())
cnt = 0
if abs(b-a) == 1 and abs(c-b) ==1:
    print(0)
elif abs(c - b) <= 2 and abs(b - a) <= 2:
    print(1)
else:
    print(max(abs(b-a), abs(c-b)) - 1)