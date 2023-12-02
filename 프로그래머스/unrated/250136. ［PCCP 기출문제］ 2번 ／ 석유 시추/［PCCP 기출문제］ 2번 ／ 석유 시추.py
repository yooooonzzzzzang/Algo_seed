from collections import deque

def solution(land):
    answer = [0] * len(land[0])
    direction = [[-1, 0], [0,1], [1,0], [0,-1]]

    for col in range(len(land[0])):
        queue = deque()
        for row in range(len(land)):
            if land[row][col] ==1:
                queue.append((row,col))
                land[row][col] = -1
            col_list = set()
            cnt = 0
            while queue:
                y, x = queue.popleft()
                cnt += 1
                col_list.add(x)
                for dy, dx in direction:
                    if 0 <= y+dy < len(land) and 0 <= x+dx < len(land[0]) and land[y+dy][x+dx] and land[y+dy][x+dx] != -1:
                        queue.append((y+dy,x+dx))
                        land[y+dy][x+dx] = -1
            for c in col_list:
                answer[c] += cnt
    ans = 0
    for i in answer:
        if i > ans:
            ans = i
    return ans