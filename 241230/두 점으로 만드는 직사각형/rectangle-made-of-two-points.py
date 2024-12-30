x1,x2,y1,y2=map(int,input().split())
x3,x4,y3,y4=map(int,input().split())
print((max(y1, y3) - min(x1,x3))*(max(y2,y4)-min(x2,x4)))