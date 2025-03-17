n, m = map(int, input().split())
lines = []
for _ in range(m):
    a, b = tuple(map(int, input().split()))
    lines.append((b, a - 1))
lines.sort()
ans = m
selected_line =[]
def possible():
    num1, num2 = [i for i in range(n)], [i for i in range(n)]
	
    # Step2. 위에서부터 순서대로 적혀있는 
    # 가로줄에 대해 양쪽 번호에 해당하는 숫자를 바꿔줍니다. 
    
    for _, idx in lines:
        num1[idx], num1[idx + 1] = num1[idx + 1], num1[idx]
    for _, idx in selected_line:
        num2[idx], num2[idx + 1] = num2[idx + 1], num2[idx]
	
    # Step3. 두 상황의 결과가 동일한지 확인합니다.
    for i in range(n):
        if num1[i] != num2[i]:
            return False

    return True

def find_min(cnt):
    global ans 
    if cnt == m:
        if possible():
            ans = min(ans, len(selected_line))
        return
    selected_line.append(lines[cnt])
    find_min(cnt+1)
    selected_line.pop()
    find_min(cnt+1)
find_min(0)
print(ans)
# 어디를 , 먼저 