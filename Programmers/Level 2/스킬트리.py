def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        idxs = []
        for s in skill:
            if s not in set(tree):
                idxs.append(float("inf"))
            else:
                idxs.append(tree.index(s))
                
        # print(tree, idxs)
        if len(idxs) == len(skill) and idxs == sorted(idxs):
            answer += 1
    
    return answer
