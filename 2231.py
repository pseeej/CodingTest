N = int(input())

res = 0

# 제일 작은 값을 구해야하므로 큰 값부터 점점 내려오도록 함
for num in range(N, 1, -1):
    # 결과값 저장 위해... 아래서 num값에 변동을 주므로 real_num으로 보존
    real_num = num

    # 계산의 첫 시작은 본인을 더하는 것!
    calc = num

    # print(num, end=" ")

    # 더이상 나눠질 값이 없을 때까지...
    # 제일 마지막 값을 계속 빼내와서 더해줌
    while num > 0:
        calc += num%10
        num = num // 10
    
    # print(calc, end=" ")

    if calc == N:
        res = real_num

    # print()


print(res)
