n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

def get_end_idx(idx, num):
    for i in range(idx+1, len(numbers)):
        if numbers[i] != numbers[idx]:
            return i-1
    return len(numbers) -1 

# 
while True:
    exploded = False

    for idx, num in enumerate(numbers):
        # 이미 터짐
        if num == 0:
            continue
        end_idx = get_end_idx(idx, num)
        if end_idx - idx + 1 >= m:
            numbers[idx:end_idx+1] = [0] * (end_idx - idx + 1 )
            exploded = True
    numbers = list(filter(lambda x:x>0, numbers))

    if not exploded:
        break

print(len(numbers))
for number in numbers:
    print(number)
