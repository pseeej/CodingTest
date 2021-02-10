n = int(input())

a = []

temp = input().split()
    
for i in temp:
    if(int(i) not in a):
        a.append(int(i))
        
a.sort()

for i in range(len(a)):
    print(a[i], end=" ")
