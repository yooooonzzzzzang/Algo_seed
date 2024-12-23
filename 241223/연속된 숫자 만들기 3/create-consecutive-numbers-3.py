a,b,c = map(int,input().split())
cnt = 0
if c - b == 2 or b - a == 2:
    print(1)
elif c - b == 3 or b - a == 3:
    print(2)
else:
    print(c-b-a)