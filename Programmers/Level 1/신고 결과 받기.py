def solution(id_list, report, k):
    # 정답 배열 초기화
    answer = [0 for i in range(len(id_list))]
    
    rep_cnt = {} # 각 id별로 report 당한 횟수 저장 위한 dict
    rep_list = {}   # 각 id별로 누구를 report 했는지를 기록 위한 dict
    
    # 초기화
    for id in id_list:
        rep_cnt[id] = 0
        rep_list[id] = set()    # 시간 단축 위해 set 사용
    
    # report list 돌면서 rep_list와 rep_cnt 채워주기
    for rep in report:
        from_id, to_id = rep.split()
        # 이전에 신고한 기록이 없을 경우에만 rep_list에 추가하고
        # rep_cnt += 1 수행
        if to_id not in rep_list[from_id]:
            rep_list[from_id].add(to_id)
            rep_cnt[to_id] += 1
        
    # report 횟수를 담고 있는 rep_cnt 돌면서
    # 정해진 횟수 k 이상인 id들만 real_rep에 저장
    real_rep = []
    for id in rep_cnt.keys():
        if rep_cnt[id] >= k:
            real_rep.append(id)
    
    # rep_list에 있는 모든 id들을 돌면서
    # real_rep에 있는 이름이 있는지 확인
    # 있을 경우 answer 배열의 정해진 위치에 +1
    for from_id in rep_list:
        for to_id in real_rep:
            if to_id in rep_list[from_id]:
                answer[id_list.index(from_id)] += 1
    
    return answer
