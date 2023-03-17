def solution(clothes):
    maps = {}
    for i,j in clothes:
        print(i,j)
        if not maps.get(j):
            maps[j] = [i]
        else:
            maps[j].append(i)

    cnt = 1
    for i in maps:
        cnt *= len(maps.get(i))+1


    return cnt-1