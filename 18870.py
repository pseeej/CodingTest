import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

idxs = dict()
for elem in arr:
    idxs[elem] = 0

sortedarr = sorted(list(set(idxs)))

for i in range(len(sortedarr)):
    idxs[sortedarr[i]] = i

for i in range(N):
    print(idxs[arr[i]], end=" ")
