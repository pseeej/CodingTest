from collections import defaultdict, deque
def solution(n, edge):
    answer = 0
    
    graph = defaultdict(set)
    for e in edge:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
        
    dist = defaultdict(lambda: float("inf"))
    nexts = deque()
    nexts.append(1)
    dist[1] = 0
    # tovisit = set(i for i in range(1, n+1))
    
    while nexts:
        now = nexts.popleft()
        for node in graph[now]:
            if dist[node] > dist[now] + 1:
                dist[node] = dist[now] + 1
                nexts.append(node)
            
    sorteddist = sorted(dist.items(), key= lambda item:item[1], reverse=True)
    maxdist = sorteddist[0][1]
    for i in range(len(sorteddist)):
        if maxdist != sorteddist[i][1]:
            break
        answer += 1
            
        
    
    
    return answer
