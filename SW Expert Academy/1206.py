for test_case in range(1, 11):
    length = int(input())
    result = 0

    apts = [0, 0]
    tmpli = list(map(int, input().split()))
    apts.extend((tmpli))
    apts.extend([0, 0])

    for mid in range(2, length+2):
        left = mid-2
        right = mid+2

        # 왼쪽 두 개 확인
        sun_left = min(apts[mid]-apts[left], apts[mid]-apts[left+1])
        # 오른쪽 두 개 확인
        sun_right = min(apts[mid]-apts[right], apts[mid]-apts[right-1])

        calc = min(sun_left, sun_right)
        if calc > 0:
            result += calc

    print(f"#{test_case} {result}")
