from collections import defaultdict

def solution(str1, str2):
    answer = 0
    
    s1cnts = defaultdict(int)
    s2cnts = defaultdict(int)
    
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            newword = str1[i]+str1[i+1]
            s1cnts[newword.lower()] += 1
            
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            newword = str2[i]+str2[i+1]
            s2cnts[newword.lower()] += 1
            
    # print(s1cnts, s2cnts)
            
    midcnt = 0
    totcnt = 0
    
    for key in s1cnts:
        if key in set(s2cnts.keys()):
            midcnt += min(s1cnts[key], s2cnts[key])
            totcnt += max(s1cnts[key], s2cnts[key])
        else:
            totcnt += s1cnts[key]
            
    for key in s2cnts:
        if key in set(s1cnts.keys()):
            continue
        else:
            totcnt += s2cnts[key]
    
    if totcnt == 0:
        return 65536
    
    answer = (midcnt/totcnt)*65536 // 1
    
    return answer
