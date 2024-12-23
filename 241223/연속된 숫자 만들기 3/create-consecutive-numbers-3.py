a,b,c = map(int,input().split())
cnt = 0
if b-a == 1 and c-b ==1:
    print(0)
elif c - b == 3 or b - a == 3:
    print(2)
elif c - b == 2 or b - a == 2:
    print(1)
else:
    print(c-b-a)