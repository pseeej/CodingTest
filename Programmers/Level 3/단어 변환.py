from collections import deque, defaultdict

def checkIfDiff1(word1, word2):
    cnt = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cnt += 1
    
    if cnt == 1:
        return True
    
    return False


def solution(begin, target, words):
    answer = 0
    
    wordlength = len(target)
    
    tovisit = deque()
    tovisit.append(begin)
    
    visited = {}
    for word in words:
        visited[word] = 10**7
        
    visited[begin] = 0
    
    while tovisit:
        # print(visited)
        now = tovisit.popleft()
        dist = visited[now]
        
        for word in words:
            # print(word, now, checkIfDiff1(now, word))
            if checkIfDiff1(now, word) and visited[word] > dist+1:
                tovisit.append(word)
                visited[word] = dist+1

    if target in visited and visited[target] != 10**7:
        return visited[target]
    
    return 0
