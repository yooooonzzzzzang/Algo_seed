def solution(elements):
    answer = 0
    long_elements = elements + elements[:len(elements)-1]
    set_hap = set()
    
    for i in range(len(elements)):
        for j in range(len(long_elements)-i):
            set_hap.add(sum(long_elements[j:j+i+1]))
    return len(set_hap)