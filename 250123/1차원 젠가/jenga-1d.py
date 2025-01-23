n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Write your code here!
tmp = []
for i in range(n):
    if i >= s1-1 and i <= e1-1:
        continue
    else:
        tmp.append(blocks[i])
blocks =[]
for i in range(len(tmp)):
    if i >= s2-1 and i <= e2-1:
        continue
    else:
        blocks.append(tmp[i])
print(len(blocks))
for i in blocks:
    print(i)