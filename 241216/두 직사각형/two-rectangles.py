x1, y1, x2, y2 = map(int,input().split())
x3, y3, x4, y4 = map(int,input().split())


if x2 < x3 or x4 < x1 or y1 > y4 or y3 > y2 :
    print("nonoverlapping")
else:
    print("overlapping")