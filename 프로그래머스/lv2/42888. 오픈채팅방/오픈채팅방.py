def solution(record):
    answer = []
    dic = {}
    
    for sentence in record:
        sentence_split = sentence.split()
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]
    
    for sentence in record:
        sentence_split = sentence.split()
        if len(sentence_split) == 2:
            answer.append(f'{dic[sentence_split[1]]}님이 나갔습니다.')
        else:
            if sentence_split[0] =="Enter":
                answer.append(f'{dic[sentence_split[1]]}님이 들어왔습니다.')
    return(answer)