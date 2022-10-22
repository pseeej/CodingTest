from collections import defaultdict, deque
def solution(n, computers):
    answer = 0
    
    nets = defaultdict(set)
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j:
                nets[i].add(j)
    
    tovisit = set(i for i in range(len(computers)))
    
    def DFS(now, tovisit):
        if now in tovisit:
            tovisit.remove(now)
        
        for next in nets[now]:
            if next in tovisit:
                tovisit.remove(next)
                tovisit = DFS(next, tovisit)
                
        return tovisit
                
    
    cnt = 0
    nexts = deque()
    for i in range(len(computers)):
        if i in tovisit:
            cnt += 1
        tovisit = DFS(i, tovisit)
                    
    print(tovisit)
    print(cnt)
    
    
    return cnt
