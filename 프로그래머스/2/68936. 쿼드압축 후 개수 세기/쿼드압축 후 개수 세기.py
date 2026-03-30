def solution(arr):
    # 0, 1 개수 
    answer = [0, 0]


    def quad(s, n):
        x, y, tg = s[0], s[1], arr[s[0]][s[1]]
        for i in range(n):
            for j in range(n):
                if arr[x+i][y+j] != tg:
                    quad([x, y], n//2)
                    quad([x, y+n//2], n//2)
                    quad([x+n//2, y], n//2)
                    quad([x+n//2, y+n//2], n//2)
                    return
        answer[tg] += 1
    quad(answer, len(arr))
    return answer