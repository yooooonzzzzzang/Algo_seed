import sys

n, m, p = tuple(map(int, input().split()))
message = [
    list(input().split())
    for _ in range(m)
]
# 예외
if message[p-1][1] == 0:
    sys.exit()

for i in range(n):
    person = chr(ord('A')+i)
    flag = False
    for c,u in message:
        if int(u) >= int(message[p-1][1]) and person == c:
            flag = True
    if not flag:
        print(person, end=" ")