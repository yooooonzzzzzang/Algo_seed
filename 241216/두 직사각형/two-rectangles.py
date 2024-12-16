x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())


if x2 < x3 or x4 < x1:
    print("nonoverlapping")
else:
    print("overlapping")