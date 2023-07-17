def solution(board, moves):
    answer = 0
    arr = []
    # 1. 31 개의 배열을 만들어서 옮기기 - 근데 거꾸로 숫자 넣기 
    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i]-1] != 0:
                if arr and arr[-1] == board[j][moves[i]-1]:
                    arr.pop()
                    answer += 2
                else:
                    arr.append(board[j][moves[i]-1])
                
                board[j][moves[i]-1] = 0
                break
    print(arr)
    # 2. moves 로 arr[i]의 pop() 하고
    # 3. arr2[-1] 과 같으면 answer += 2 아니면 append(arr[i])
    return answer