def solution(s):
    answer = []
    zeroCnt = 0
    changeCnt = 0
    while s != '1':
        oneCnt = 0
        for i in s:
            if i == '0':
                zeroCnt+=1
            else:
                oneCnt+=1
        # 이진 변화해주기
        stack = []
        while oneCnt:
            na = oneCnt % 2
            stack.append(na)
            oneCnt = oneCnt//2
            if oneCnt == 1:
                stack.append(1)
                break
        s =''
        for i in range(len(stack)-1,-1,-1):
            s = s + str(stack[i])
        changeCnt += 1
    answer.append(changeCnt)
    answer.append(zeroCnt)
    return answer