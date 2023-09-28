for _ in range(int(input())):
    num = int(input())
    for i in range(2, 1000002):
        if num % i == 0:
            print("NO")
            break
        if i == 1000001:
            print("YES")