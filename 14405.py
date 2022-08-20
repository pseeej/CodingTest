sent = input()
pikachu = ["pi", "ka", "chu"]

idx = 0
while True:
    if sent[idx:idx+2] in pikachu:
        idx += 2
    elif sent[idx:idx+3] in pikachu:
        idx += 3
    else:
        print("NO")
        break
        
    if idx >= len(sent):
        print("YES")
        break
