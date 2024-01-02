import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    costs = list(map(int, input().split()))
    result = 0

    backmax = costs[-1]
    bought = []
    for i in range(N-1, 0, -1):
        if costs[i-1] <= costs[i]:
            bought.append(costs[i-1])
            
        elif costs[i-1] > costs[i] and costs[i-1] > backmax:
            for buy in bought:
                result += backmax - buy
            backmax = costs[i-1]
            bought = []

        elif costs[i-1] >= costs[i] and costs[i-1] < backmax:
            bought.append(costs[i-1])

        # print(bought)


    for buy in bought:
        result += backmax - buy

    print(result)
