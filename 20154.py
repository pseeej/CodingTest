alphadict = {"A" : 3, "B" : 2, "C" : 1, "D" : 2, "E" : 3, "F" : 3, "G" : 3, "H" : 3, "I" : 1, "J" : 1, "K" : 3, "L" : 1, "M" : 3, "N" : 3, "O" : 1, "P" : 2, "Q" : 2, "R" : 2, "S" : 1, "T" : 2, "U" : 1, "V" : 1, "W" : 2, "X" : 2, "Y" : 2, "Z" : 1}

sent = input()
alpha2num = []

for c in sent:
    alpha2num.append(alphadict[c])

while len(alpha2num) > 1:
    tmpList = []
    for i in range(0, len(alpha2num)-1, 2):
        tmpList.append((alpha2num[i] + alpha2num[i+1])%10)

    # 홀수일 때 나머지 하나의 값도 덧붙여주기
    if len(alpha2num) % 2 == 1:
        tmpList.append(alpha2num[-1])
    alpha2num = tmpList

if alpha2num[0] % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
