def check(x1,x2,x3,x4):
    flag = True
    if x2 < x3 or x1 > x4:
        flag = False 
    return 'intersecting' if flag else 'nonintersecting'

print(check(*map(int,input().split())))
