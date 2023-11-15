def solution(s):
    answer = []
    tuples = []
    
    s = s[1:-1]
    s = s.split('}')[:-1]
    
    
    for i in range(len(s)):
        if s[i][0] == ',':
            s[i] = s[i][2:]
        else:
            s[i] = s[i][1:]
            
        s[i] = list(map(int, s[i].split(',')))
            
    s = sorted(s, key=lambda s:len(s))
    
    alreadynum = []
    
    # print(s)
    
    for tup in s:
        if len(tup) == 1:
            alreadynum.append(tup[0])
            continue
        
        for i in range(len(tup)):
            if tup[i] not in alreadynum:
                alreadynum.append(tup[i])
    
        
    
    return alreadynum
