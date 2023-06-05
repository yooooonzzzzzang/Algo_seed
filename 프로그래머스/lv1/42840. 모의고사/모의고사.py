two_C  = [2,1,2,3,2,4,2,5]
three_C = [3,3,1,1,2,2,4,4,5,5]
def solution(answers):
    answer = []

    def one():
        cnt = 0
        for i in range(len(answers)):
            a = i % 5 +1
            if answers[i] == a:
                cnt +=1
        return cnt

    def two():
        cnt = 0
        for i in range(len(answers)):
            if answers[i] == two_C[i % 8]:
                cnt += 1
        return cnt

    def three():
        cnt = 0
        for i in range(len(answers)):
            if answers[i] == three_C[i % 10]:
                cnt += 1
        return cnt

    answer.append((1,one()))
    answer.append((2,two()))
    answer.append((3,three()))

    real =[]
    answer.sort(key=lambda x:x[1], reverse=True)
    for i in range(len(answer)):
            if answer[i][1] == answer[0][1]:
                real.append(answer[i][0])
    print(real)
    return real