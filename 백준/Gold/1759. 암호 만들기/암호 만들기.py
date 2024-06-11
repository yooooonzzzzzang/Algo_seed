
def dfs(level, start):
    if level == l:
        v_cnt =0
        l_cnt =0
        for i in tmp:
            if i in vowels:
                v_cnt += 1
            else:
                l_cnt += 1
        if v_cnt >=1 and l_cnt >= 2:
            print(''.join(tmp))
    else:
        for i in range(start, c):
            tmp[level] = arr[i]
            dfs(level+1, i+1)
            tmp[level] = 0
            


l,c = map(int,input().split())
arr = sorted(input().split())
tmp = [0] * l
vowels = 'aeiou'
dfs(0,0)

# 모음 1개 이상 자음 2개 이상
