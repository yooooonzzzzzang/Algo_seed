import math
def solution(n, words):
    answer = []
    q = []
    # 탈락하는경우: 이미 나온 단어를 말한경우, 이전 단어 마지막 글자로 시작하지 않는 경우
    for i in range(len(words)):
        if not q:
            q.append(words[i])
        else:
            if words[i][0] != q[-1][-1] or words[i] in q:
                # idx, 몇번째 
                return [i%n+1, i//n+1]
            else:
                q.append(words[i])
    # break 안됐으면 끝말잇기 잘함
    else:
        return [0,0]
