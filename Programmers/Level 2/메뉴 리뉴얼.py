from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []

    # course에 들어갈 수 있는 개수에 따라 for문 돌음
    for c in course:
        # 조합들을 저장할 dictionary의 value값들을 0으로 설정
        allcomb = defaultdict(lambda:0)
        # 모든 order들에 대해 조합을 진행해주었다.
        for o in range(len(orders)):
            print(type(combinations(orders[o], c)))
            combli = list(combinations(orders[o], c))
            # 나온 조합에 대해 알파벳 순서대로 정렬
            # 이미 나왔던 조합일 경우 +1 (사실 아니어도 +1임. defaultdict 이용해서.)
            for comb in combli:
                ch_comb = list(comb)
                ch_comb.sort()
                # list를 string 형태로 변환하려고 할 땐 .join 사용
                ch_comb = ''.join(ch_comb)
                allcomb[ch_comb] += 1
        
        # 각 조합에서 가장 많이 나온 조합이 몇 번 나왔는지 알아내기 위함
        maxlen = max(list(allcomb.values()), default=0)
        
        # 최소 두 번 이상 나왔어야 하므로 주어진 조건에서
        # max값과 같은 조합들을 최종 answer로 넣어준다.
        if maxlen >= 2:
            for c in allcomb.keys():
                if allcomb[c] == maxlen:
                    answer.append(c)
    
    answer.sort()
    
    return answer
