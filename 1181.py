def swap(words, i, j):
    tmp = words[i]
    words[i] = words[j]
    words[j] = tmp

N = int(input())

words = []

# 중복 제거
words_set = set()
for _ in range(N):
    words_set.add(input())

for word in words_set:
    words.append(word)

for i in range(len(words)-1):
    for j in range(i+1, len(words)):
        if len(words[i]) > len(words[j]):
            swap(words, i, j)
        elif len(words[i]) == len(words[j]) and words[i] > words[j]:
            swap(words, i, j)

for word in words:
    print(word)
