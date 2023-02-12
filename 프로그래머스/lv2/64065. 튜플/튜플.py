def solution(s):
    answer = []
    a = s.split("},{")
    for i in range(len(a)):
        if "{{" in a[i] :
            a[i] = a[i].replace("{{",'')
        if "}}" in a[i]:
            a[i] = a[i].replace("}}",'')
    a.sort(key=len)
    for list in a:
        if "," in list:
            j = list.split(",")
            for jj in j:
                if int(jj)  not in answer:
                    answer.append(int(jj))
        else:
            if int(list)  not in answer:
                answer.append(int(list))

    return answer