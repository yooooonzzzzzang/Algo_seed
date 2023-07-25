def solution(strings, n):
    # 같은 문자일 경우를 위해 미리 정렬
    strings.sort() 
    return sorted(strings, key=lambda x:x[n])