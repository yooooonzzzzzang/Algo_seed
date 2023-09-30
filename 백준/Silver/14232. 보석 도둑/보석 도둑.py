n = int(input())
k = []


for i in range(2, int(n**0.5)+1):
    while n % i == 0:
        k.append(i)
        n = n // i

if n != 1:
    k.append(n)
print(len(k))
print(*k)

