from collections import defaultdict, deque
def solution(n, wires):
    answer = float("inf")
    
    graph = defaultdict(set)
    
    for wire in wires:
        left, right = wire[0], wire[1]
        
        graph[left].add(right)
        graph[right].add(left)
        
    for wire in wires:
        left, right = wire[0], wire[1]
        
        visited = set()
        visited.add(left)
        visited.add(right)
        
        ##### 왼쪽 #######
        leftdeq = deque()
        leftdeq.append(left)
        leftcnt = 0
        
        while leftdeq:
            left = leftdeq.popleft()
            for node in graph[left]:
                if node not in visited:
                    leftdeq.append(node)
                    visited.add(node)
            
            leftcnt += 1
            
        ##### 오른쪽 #######
        rightdeq = deque()
        rightdeq.append(right)
        rightcnt = 0
        
        while rightdeq:
            right = rightdeq.popleft()
            for node in graph[right]:
                if node not in visited:
                    rightdeq.append(node)
                    visited.add(node)
            
            rightcnt += 1
            
        answer = min(answer, max(leftcnt, rightcnt)-min(leftcnt, rightcnt))
        # print(leftcnt, rightcnt)
            
    
    return answer
