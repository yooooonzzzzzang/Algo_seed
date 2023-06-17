def solution(quiz):
    answer = []
    for i in quiz:
        sik, ans = i.split("=")
        if eval(sik) == int(ans):
            answer.append("O")
        else: answer.append("X")
    return answer