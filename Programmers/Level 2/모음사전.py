from itertools import product

def solution(word):
    answer = 0
    
    ondict = []
    for i in range(1, 6):
        ondict.extend(list(product('AEIOU', repeat=i)))
    
    ondict.sort()
    # print(ondict[:30])
    findw = []
    for w in word:
        findw.append(w)
    findw = tuple(findw)
    answer = ondict.index(findw)+1
    
    return answer
