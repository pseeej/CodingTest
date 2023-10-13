from collections import deque, defaultdict
import sys
input = sys.stdin.readline

N = int(input())
likes = dict()
turn = deque()

for _ in range(N**2):
    tmp = list(map(int, input().split()))
    likes[tmp[0]] = set(tmp[1:])
    turn.append(tmp[0])

board = [[0 for _ in range(N)] for _ in range(N)]
done = dict()

while turn:

    # print()
    # for i in range(N):
    #     for j in range(N):
    #          print(board[i][j], end=" ")
    #     print()

    now = turn.popleft()
    available = defaultdict(int)

    # 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 정하기
    # 좋아하는 학생이 보드에 있을 경우
    for friend in likes[now]:        
        if friend in done:
            y, x = done[friend]
            for i, j in [(1,0), (0, 1), (-1, 0), (0, -1)]:
                if y+i >= 0 and y+i < N and x+j >= 0 and x+j < N and board[y+i][x+j] == 0:
                    available[(y+i, x+j)] += 1

    # 좋아하는 학생이 보드에 없을 경우
    else:
        for i in range(N):
            for j in range(N):
                if board[i][j] == 0:
                    available[(i, j)] += 1

    # 인접한 칸에 가장 많은 칸 찾기
    std = max(available.values())
    keys = list(available.keys())
    for point in keys:
        if available[point] != std:
            available.pop(point)

    # print("available: ", available)

    if len(available) == 1:
        y, x = list(available.keys())[0]
        board[y][x] = now
        done[now] = (y, x)
        continue

    # 여러 개라면 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 정하기
    empty = defaultdict(int)
    for point in available:
        y, x = point
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if y+i >= 0 and y+i < N and x+j >= 0 and x+j < N and board[y+i][x+j] == 0:
                empty[point] += 1

    # print("empty: ", empty)

    if len(empty):
        std = max(empty.values())
        for point in empty:
            if empty[point] != std:
                available.pop(point)

        keys = list(available.keys())
        for point in keys:
            if point not in empty:
                available.pop(point)

    # else:
    #     for i in range(N):
    #         for j in range(N):
    #             if board[i][j] == 0:
    #                 available[(i, j)] += 1


    # print("available: ", available)

    if len(available) == 1:
        y, x = list(available.keys())[0]
        board[y][x] = now
        done[now] = (y, x)
        continue

    # 여러 개라면 행의 번호가 가장 작은 칸으로, 그러고도 여러 개면 열의 번호가 가장 작은 칸으로
    sorted_dict = sorted(available.keys(), key=lambda x:(x[0], x[1]))
    y, x = sorted_dict[0]
    board[y][x] = now
    done[now] = (y, x)

# print()
# for i in range(N):
#     for j in range(N):
#         print(board[i][j], end=" ")
#     print()

result = 0
            
for y in range(N):
    for x in range(N):
        now = board[y][x]

        cnt = 0
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if y+i >= 0 and y+i < N and x+j >= 0 and x+j < N and board[y+i][x+j] in likes[now]:
                cnt += 1
        
        if cnt == 0:
            result += 0
        elif cnt == 1:
            result += 1
        elif cnt == 2:
            result += 10
        elif cnt == 3:
            result += 100
        elif cnt == 4:
            result += 1000

print(result)









