temp = input().split()
num1 = int(temp[0])

A = []
temp = input().split()
for i in temp:
    A.append(int(i))
    
B = []
temp = input().split()
for i in temp:
    B.append(int(i))

A = set(A)
B = set(B)

listAB = list(A-B)
listBA = list(B-A)

print(len(listAB)+len(listBA))
