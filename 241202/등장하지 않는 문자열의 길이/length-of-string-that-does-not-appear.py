# print(ord('A'))
# print(ord('Z'))
arr = [0] * 26
n = int(input())
inputs = input()
length = 0
ans = 200
for i in range(n):
    if arr[ord(inputs[i]) - 65] == 0:
        length += 1
        arr[ord(inputs[i]) - 65] += 1
    else:
        ans = min(length, ans)
        length = 0
        arr = [0] * 26
        arr[ord(inputs[i]) - 65] += 1

print(ans)
