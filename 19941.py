import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = input()

hams = set()
person = []
result = 0

for i in range(N):
    if arr[i] == "H":
        hams.add(i)
    else:
        person.append(i)
# print(person, hams)
for p in person:
    checkIfDone = False
    for i in range(K, 0, -1):
        if p-i in hams:
            checkIfDone = True
            hams.remove(p-i)
            result += 1 
            # print(p, p-i)
            break

    if checkIfDone:
        continue

    for i in range(1, K+1):
        if p+i in hams:
            checkIfDone = True
            hams.remove(p+i)
            result += 1
            # print(p, p+i)
            break

    if checkIfDone:
        continue

print(result)
