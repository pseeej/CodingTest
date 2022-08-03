N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    chars = set()

    prev_char = word[0]
    ret = 1
    for i in range(1, len(word)):
        if prev_char != word[i]:
            if word[i] not in chars:
                chars.add(prev_char)
            else:
                ret = 0
                break
        
        prev_char = word[i]

    if ret == 1:
        cnt += 1


print(cnt)
