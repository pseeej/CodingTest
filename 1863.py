import sys
input = sys.stdin.readline

N = int(input())

buildings = []
for _ in range(N):
    buildings.append(list(map(int, input().split())))

# print(buildings)

counted = set()
groups = []
for i in range(N):
    curr = buildings[i]
    if tuple(curr) in counted:
        continue

    group = [curr]
    counted.add(tuple(curr))
    for j in range(i+1, N):
        if buildings[j][1] > curr[1]:
            pass
        elif buildings[j][1] == curr[1]:
            counted.add(tuple(buildings[j]))
            group.append(buildings[j])
        else:
            break

    groups.append(group)

answer = 0
for group in groups:
    if group[0][1] == 0:
        continue
    else:
        answer += 1

print(answer)
            
