def solution(answers):
    answer = []
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    c1,c2,c3 = 0,0,0
    
    for i in range(len(answers)):
        if answers[i] == s1[i%5]:
            c1+=1
        if answers[i] == s2[i%8]:
            c2+=1
        if answers[i] == s3[i%10]:
            c3+=1
    max_score = max(c1, c2, c3)
    print(max_score, c1,c2,c3)
    if max_score == c1:
        answer.append(1)
    if max_score == c2:
        answer.append(2)
    if max_score == c3:
        answer.append(3)
    return answer