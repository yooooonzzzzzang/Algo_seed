def solution(new_id):
    answer = ''
    # . 처음 & 끝 x , 연속 x
    munja = ['-','_','.']
    # 1 단계
    new_id = new_id.lower()
    # 2 단계
    tmp = ''
    for i in new_id:
        if i.isalnum() == False:
            if i in munja:
                tmp += i
        else:
            tmp += i
    new_id = tmp
    print(new_id,"2단계")
    # 3 단계
    tmp = ''
    prev_char = ''

    # 반복문을 통해 문자열 검사
    for char in new_id:
        # 이전 문자와 현재 문자가 모두 마침표인 경우, 건너뜀
        if prev_char == '.' and char == '.':
            continue

        # 아닌 경우, 현재 문자를 추가
        tmp += char
        prev_char = char
    new_id = tmp
    print(new_id,"3단계")
    # 4 단계
    new_id = new_id.strip('.')
    print(new_id,"4단계")
    # 5 단계
    if not new_id:
        new_id = "a"
    
    print(new_id,"5단계")
    # 6 단계
    if len(new_id)>=16:
        new_id = new_id[:15]
        if new_id[-1] =='.':
            new_id = new_id[:-1]
    print(new_id,"6단계")
    # 7 단계
    if len(new_id) <= 2 and len(new_id)>=1:
        while len(new_id) <3:
            new_id += new_id[-1]
    print(new_id,"7단계")
    #     while len(new_id) <= 3:
    #         new_id += new_id[-1]
    
    return new_id