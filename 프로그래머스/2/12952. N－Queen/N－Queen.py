def solution(n):
    global answer
    answer = 0

    def is_available(candidate, current_col):
        current_row = len(candidate)
        for queen_row in range(current_row):
            if candidate[queen_row] == current_col or abs(candidate[queen_row]-current_col) == current_row - queen_row:
                return False
        return True

    def DFS(n,current_row, current_candidate):
        global answer
        if current_row == n:
            answer+=1;  # 개수 +1
            return
        for candidate_col in range(n):
            if is_available(current_candidate, candidate_col):
                current_candidate.append(candidate_col)
                DFS(n,current_row+1, current_candidate)
                current_candidate.pop()
    DFS(n,0,[])
    return answer