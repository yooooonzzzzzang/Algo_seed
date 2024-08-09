from collections import Counter
str = input()
str = str.upper()
counter = Counter(str)

if len(counter.most_common()) > 1 :
    if counter.most_common(1)[0][1] == counter.most_common(2)[1][1]:
        print("?")
    else:
        print(counter.most_common(1)[0][0])
else:
    print(counter.most_common(1)[0][0])