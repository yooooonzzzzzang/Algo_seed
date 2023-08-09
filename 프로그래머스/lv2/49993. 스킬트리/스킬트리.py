
def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        q = ''
        for sk in i:
            if sk in skill:
                q += sk
        if not q:
            answer += 1
        else:
            if skill.startswith(q):
                answer+=1   
    return answer