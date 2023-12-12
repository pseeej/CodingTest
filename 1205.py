import sys
input = sys.stdin.readline

N, newscore, P = map(int, input().split())
scores = []
if N > 0:
    scores = list(map(int, input().split()))

result = 0
for i in range(N):
    if scores[i] >= newscore:
        result = i+1


scores = scores[:result] + [newscore] + scores[result:]
# print(scores)

# result가 idx임

if result >= P:
    print(-1)
else:
    rank = 1
    for i in range(result+1):
        if scores[i] == newscore:
            print(i+1)
            break
