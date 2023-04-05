for _ in range(10):
    test_case = int(input())
    findstr = input()
    sent = input()

    cnt = 0

    for i in range(len(sent)-len(findstr)+1):
        if sent[i] == findstr[0] and sent[i:i+len(findstr)] == findstr:
            cnt += 1

    print(f"#{test_case} {cnt}")

