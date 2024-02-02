from copy import deepcopy
import sys
input = sys.stdin.readline

N = int(input())
tmp1 = input().strip()
tmp2 = input().strip()

origin = []
renovated = []
for i in range(N):
    if tmp1[i] == '0':
        origin.append(False)
    else:
        origin.append(True)

    if tmp2[i] == '0':
        renovated.append(False)
    else:
        renovated.append(True)

real = deepcopy(origin)

noclick = 0

# 만약 0에서 클릭하지 않았다면
for i in range(1, N):
    # print(i, origin, end=" -> ")
    # 동일하다면 넘어가기
    if origin[i-1] == renovated[i-1]:
        # print()
        continue

    # 다르다면
    j = i-1
    while j < i+2 and j < N:
        origin[j] = not origin[j]
        j += 1
    noclick += 1
    # print(origin)

if origin[-1] != renovated[-1]:
    noclick = -1

origin = deepcopy(real)
# print()

clicked = 1
# 만약 0에서 클릭했다면
origin[0] = not origin[0]
origin[1] = not origin[1]
for i in range(1, N):
    # print(i, origin, end=" -> ")
    if origin[i-1] == renovated[i-1]:
        # print()
        continue

    j = i-1
    while j < i+2 and j < N:
        origin[j] = not origin[j]
        j+=1
    clicked += 1

    # print(origin)

if origin[-1] != renovated[-1]:
    clicked = -1


# print(clicked, noclick)
if clicked == -1 and noclick == -1:
    print(-1)
elif clicked != -1 and noclick == -1:
    print(clicked)
elif clicked == -1 and noclick != -1:
    print(noclick)
else:
    print(min(clicked, noclick))
            
