def solution(sequence, k):
    answer = [0, 1000001]

    sums = list(sequence)
    for i in range(1, len(sequence)):
        sums[i] = sums[i-1]+sequence[i]
    sums.insert(0, 0)

    left = 0
    right = 0
    # print(sums)
    while True:
        if sums[right]-sums[left] == k:
            if answer[1]-answer[0] > right-1-left:
                answer = [left, right-1]
            right += 1
        elif sums[right] - sums[left] < k:
            right += 1
        elif sums[right] - sums[left] > k:
            left += 1

        # print(left, right, answer)

        if right >= len(sums) or left >= right:
            break
    
    return answer
