def solution(n, words):
    tt = []
    for i in range(len(words)):
        player = i % n +1
        player_cnt = i //n + 1
        # 단어 중복 체크 -> return
        if words[i] in tt:
            return [player, player_cnt]
        else:
            tt.append(words[i])
        # 이전 단어 끝과 현재 단어 처음 글자 비교 -> return
        if i != 0:
            if tt[-1][0] != words[i-1][-1]:
                return [player, player_cnt]
    return [0,0]