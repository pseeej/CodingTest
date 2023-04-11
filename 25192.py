import sys
input = sys.stdin.readline

N = int(input())
ids = set()
cnt = 0

for _ in range(N):
    sent = input().strip()
    if sent == "ENTER":
        ids = set()
    elif sent not in ids:
        ids.add(sent)
        cnt += 1

print(cnt)
    
