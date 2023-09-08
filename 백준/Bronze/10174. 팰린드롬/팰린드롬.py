t = int(input())
for _ in range(t):
    s = input().lower()
    s2 = s[::-1]
    if s == s2:
        print("Yes")
    else:
        print("No")
