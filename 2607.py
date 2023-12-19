import sys
from collections import defaultdict
from copy import deepcopy
input = sys.stdin.readline

N = int(input())
std = input().strip()
std_d = defaultdict(int)
answer = 0

for c in std:
    std_d[c] += 1

rstd_d = deepcopy(std_d)

for _ in range(N-1):
    std_d = deepcopy(rstd_d)
    word = input().strip()

    word_d = defaultdict(int)

    for w in word:
        word_d[w] += 1

    checkIfDone = False

    alphas = list(word_d.keys())
    for w in alphas:
        if w in std_d.keys() and std_d[w] == word_d[w]:
            word_d.pop(w)
            std_d.pop(w)
        elif w in std_d.keys() and max(std_d[w], word_d[w]) - min(std_d[w], word_d[w]) > 1:
            checkIfDone = True
            break
        elif w in std_d.keys() and max(std_d[w], word_d[w]) - min(std_d[w], word_d[w]) == 1:
            if std_d[w] > word_d[w]:
                std_d[w] = 1
                word_d.pop(w)
            else:
                word_d[w] = 1
                std_d.pop(w)
        elif w not in std_d.keys() and word_d[w] > 1:
            checkIfDone = True
            break
        

    if checkIfDone:
        continue

    if len(std_d) + len(word_d) <= 1:
        # print(word)
        answer += 1
    elif len(std_d) == len(word_d) == 1:
        # print(word)
        answer += 1


print(answer)
