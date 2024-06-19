from itertools import product
import sys
input = sys.stdin.readline

channel = int(input())
_ = int(input())
if _ > 0:
    errors = list(map(int, input().split()))
else:
    errors = []
result = float("inf")

if channel == 100:
    print(0)
    exit()

checkIfTrue = True
for num in str(channel):
    num = int(num)
    if num in set(errors):
        checkIfTrue = False
        break
if checkIfTrue:
    if channel >= 100:
        print(min(channel-100, len(str(channel))))
    else:
        print(min(len(str(channel)), 100-channel))
    exit()

valids = []
for i in range(10):
    if i not in errors:
        valids.append(i)

pros = []
for i in range(1, 7):
    pros.extend(list(product(valids, repeat=i)))

newpros = []
for elem in pros:
    newnum = "".join(map(str, elem))
    newpros.append(int(newnum))

newpros.append(channel)
newpros = list(set(newpros))
newpros.sort()

idx = newpros.index(channel)
if idx-1 >= 0:
    result = min(result, channel-newpros[idx-1]+len(str(newpros[idx-1])))
if idx+1 < len(newpros):
    result = min(result, newpros[idx+1]-channel+len(str(newpros[idx+1])))

# print(newpros)

if channel < 100:
    result = min(result, 100-channel)
else:
    result = min(result, channel-100)

print(result)
