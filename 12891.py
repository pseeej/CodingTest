from collections import defaultdict
import sys
input = sys.stdin.readline

S, P = map(int, input().split())
candidate = input()

pattern = dict()
dna = "ACGT"
freq = list(map(int, input().split()))

for i in range(4):
    pattern[dna[i]] = freq[i]

result = 0

cnt = defaultdict(int)
for i in range(P):
    cnt[candidate[i]] += 1

tmp = 0
for d in dna:
    if cnt[d] >= pattern[d]:
        tmp += 1

if tmp == 4:
    result += 1

for i in range(1, S-P+1):
    cnt[candidate[i-1]] -= 1
    cnt[candidate[i+P-1]] += 1

    tmp = 0
    for d in dna:
        if cnt[d] >= pattern[d]:
            tmp += 1

    if tmp == 4:
        result += 1

print(result)
