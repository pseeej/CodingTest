import sys
input = sys.stdin.readline

code = [[None] for _ in range(8)]
length = 0

for _ in range(5):
    line = input()
    if length == 0:
        length = len(line)//4

    for i in range(length):
        code[i].append(line[:3])
        line = line[4:]

for i in range(length):
    code[i].pop(0)

for i in range(length, 8):
    code.pop()

numbers = {0:['***', '* *', '* *', '* *', '***'], 1:['  *', '  *', '  *', '  *', '  *'], 2:['***', '  *', '***', '*  ', '***'], 3:['***', '  *', '***', '*  ', '***'], 4:['* *', '* *', '***', '  *', '  *'], 5:['***', '*  ', '***', '  *', '***'], 6:['***', '*  ', '***', '* *', '***'], 7:['***', '  *', '  *', '  *', '  *'], 8:['***', '* *', '***', '* *', '***'], 9:['***', '* *', '***', '  *', '***']}

calc = ""
for i in range(length):
    for num in range(10):
        if code[i] == numbers[num]:
            calc += str(num)
            break

if int(calc)%6 == 0:
    print("BEER!!")
else:
    print("BOOM!!")
