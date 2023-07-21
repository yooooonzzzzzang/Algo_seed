def solution(s):
    s = s.lower()
    arr = []
    tmp = 0 
    # 이전 문자가 공백이고 다음은 공백이 아닐때까지 자르기
    for i in range(len(s)-1):
        if s[i] == ' ' and s[i+1] != ' ':
            arr.append(s[tmp:i+1])
            tmp = i+1
    # 마지막 문자열 추가
    arr.append(s[tmp:])
    
    for i in range(len(arr)):
        if not arr[i][0].isnumeric():  # 맨 앞 글자가[0] 숫자가 아니면
            arr[i] = arr[i].title()    # 대문자
    return ''.join(arr)        
