N, M = map(int, input().split())
dnas = []

for _ in range(N):
    dnas.append(input())

res = ""

for i in range(M):
    # ATGC 개수 세어주기 위한 딕셔너리
    neucl = dict()
    neucl['A'] = 0
    neucl['T'] = 0
    neucl['G'] = 0
    neucl['C'] = 0

    for j in range(N):
        # 현재 위치에 따른 개수 세어주기
        # 2중반복문 범위 확인!
        neucl[dnas[j][i]] += 1

    # dictionary value 값으로 정렬
    sorted_neucl = sorted(neucl.items(), key = lambda item: item[1], reverse=True)
    alpha = sorted_neucl[0][0]
    # 개수 같을 때, 알파벳 앞에 있는 걸로 사용하기! 조건 처리 위한 반복문
    for i in range(1, 4):
        if sorted_neucl[0][1] == sorted_neucl[i][1] and sorted_neucl[i][0] < alpha:
            alpha = sorted_neucl[i][0]

    res += alpha

print(res)

# hamming distance의 합 구하기 위한 과정
hamming = dict()
for i in range(N):
    hamming[dnas[i]] = 0

for i in range(N):
    for j in range(M):
        if dnas[i][j] != res[j]:
            hamming[dnas[i]] += 1

dist_sum = 0
for dist in hamming.values():
    dist_sum += dist

print(dist_sum)
# print(sum(hamming.values()))

