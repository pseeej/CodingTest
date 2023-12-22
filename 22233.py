import sys
input = sys.stdin.readline

N, M = map(int, input().split())
keywords = set()
for _ in range(N):
    keywords.add(input().strip())

for _ in range(M):
    written = list(map(str, input().split(",")))
    written[-1] = written[-1].strip()

    for word in written:
        # print(word)
        if word in keywords:
            keywords.remove(word)

    print(len(keywords))

