import sys
input = sys.stdin.readline

N = int(input())
dists = list(map(int, input().split()))
prices = list(map(int, input().split()))

res = prices[0]*dists[0]
min_price = prices[0]

for i in range(1, N-1):
    if min_price <= prices[i]:
        res += min_price*dists[i]
    else:
        min_price = prices[i]
        res += min_price*dists[i]

print(res)
