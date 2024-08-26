t = int(input())  # 테스트 케이스 수
for i in range(t):
    tmp = list(map(int, input().split()))
    arr = tmp[1:]  # 첫 번째 값은 무시하고 나머지를 사용
    ans = 0
    
    line = []  # 학생들이 줄 서는 리스트
    
    for height in arr:
        # 자신보다 큰 학생이 처음 나오는 위치를 찾기
        pos = len(line)  # 기본적으로 맨 뒤에 서는 것으로 설정
        for j in range(len(line)):
            if line[j] > height:
                pos = j
                break
        # 학생을 줄에 삽입
        line.insert(pos, height)
        # 삽입으로 인해 뒤로 물러선 학생의 수를 계산
        ans += len(line) - pos - 1
    
    print(i + 1, ans)
