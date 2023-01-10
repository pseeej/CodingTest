import sys
input = sys.stdin.readline

sent = input().strip()
words = set()

for length in range(len(sent)):
    for idx in range(len(sent)):
        words.add(sent[idx:idx+length])

print(len(words))
