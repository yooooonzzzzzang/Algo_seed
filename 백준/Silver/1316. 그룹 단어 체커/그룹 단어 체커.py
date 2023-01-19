n = int(input())
cnt = 0
for _ in range(n):
    words = input()
    wordlen = len(words)
    arr = []

    for i in range(wordlen):
        if words[i] not in arr:
            arr.append(words[i])
        else:
            # 안되는 애들
            if words[i-1] != words[i]:
                cnt += 1
                break

print(n-cnt)
