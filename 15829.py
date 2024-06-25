import sys
input = sys.stdin.readline

L = int(input())
alphas = input().strip()

result = 0
for i in range(L):
    # print((int(ord(alphas[i]))-96)*(31**(i)))
    result += (int(ord(alphas[i]))-96)*(31**(i))

print(result%1234567891)
