from collections import Counter
import math
def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    counter1 = Counter(cheori(str1))
    counter2 = Counter(cheori(str2))
    
    
    if len(counter1)==0 and len(counter2)==0:
          return 65536
    else:
        answer = len(list((counter1&counter2).elements()))/len(list((counter1|counter2).elements()))
        return int(answer*65536)
        


def cheori(str):
    arr = []
    for i in range(len(str)-1):
        if str[i].isalpha() and str[i+1].isalpha():
            two = str[i]+str[i+1]
            arr.append(two)
    return arr
        