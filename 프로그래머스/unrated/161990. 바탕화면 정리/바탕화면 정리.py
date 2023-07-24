def solution(wallpaper):
    answer = []
    arr = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                arr.append((i,j))
                arr.append((i+1,j+1))
    answer.append(min(arr, key=lambda x:x[0])[0])
    answer.append(min(arr, key=lambda x:x[1])[1])
    answer.append(max(arr, key=lambda x:x[0])[0])
    answer.append(max(arr, key=lambda x:x[1])[1])
    return answer