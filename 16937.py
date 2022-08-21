H, W = map(int, input().split())
N = int(input())

stkrs = []

# 입력과 동시에 확인해보고 안될 것 같은 애들은 제거하기
for _ in range(N):
    r, c = map(int, input().split())
    # 이미 한 쪽이라도 길이가 가로세로 둘 다 보다 클 때 제거
    if r > H and r > W:
        continue
    elif c > H and c > W:
        continue
    # 스티커의 넓이가 판의 넓이보다 클 경우 제거
    elif r*c >= W*H:
        continue
    else:
        stkrs.append([r,c])

# 남은 스티커가 2개 이하일 때 0 출력
if len(stkrs) < 2:
    print("0")
    exit()

maxarea = 0

for i in range(len(stkrs)-1):
    r1, c1 = stkrs[i]
    for j in range(i+1, len(stkrs)):
        r2, c2 = stkrs[j]

        # 회전의 경우 생각해서 가로가 c1, c2, 세로가 r1, r2
        if (c1 <= W and c2 <= W and r1+r2 <= H) or (c1+c2 <= W and r1+r2 <= H) or (c1+c2 <= W and r1 <= H and r2 <= H):
            area = c1*r1 + c2*r2
            if maxarea < area:
                maxarea = area
        # 회전의 경우 생각해서 가로가 c1, r2, 세로가 r1, c2
        elif (c1 <= W and r2 <= W and r1+c2 <= H) or (c1+r2 <= W and r1+c2 <= H) or (c1+r2 <= W and r1 <= H and c2 <= H):
            area = c1*r1 + c2*r2
            if maxarea < area:
                maxarea = area
        # 회전의 경우 생각해서 가로가 r1, c2, 세로가 c1, r2
        elif (r1 <= W and c2 <= W and c1+r2 <= H) or (r1+c2 <= W and c1+r2 <= H) or (r1+c2 <= W and c1 <= H and r2 <= H):
            area = c1*r1 + c2*r2
            if maxarea < area:
                maxarea = area
        # 회전의 경우 생각해서 가로가 r1, r2, 세로가 c1, c2
        elif (r1 <= W and r2 <= W and c1+c2 <= H) or (r1+r2 <= W and c1+c2 <= H) or (r1+r2 <= W and c1 <= H and c2 <= H):
            area = c1*r1 + c2*r2
            if maxarea < area:
                maxarea = area

print(maxarea)
