


arr = [list(input()) for _ in range(10)]
start = (0,0)
end = (0,0)
avoid = (0,0)
for i in range(10):
    for j in range(10):
        if arr[i][j] == 'B':
            end = (i,j)
        elif arr[i][j] == 'L':
            start = (i,j)
        elif arr[i][j] == 'R':
            avoid = (i,j)
if start[0]== end[0]and end[0] == avoid[0] and start[1] < avoid[1] and avoid[1] < end[1]:
    print(abs(end[0]-start[0]) + abs(end[1]- start[1]) +1)
elif start[1]== end[1]and end[1] == avoid[1]and start[0] < avoid[0] and avoid[0] < end[0]:
    print(abs(end[0]-start[0]) + abs(end[1]- start[1]) +1)
else:
    print(abs(end[0]-start[0]) + abs(end[1]- start[1]) -1)