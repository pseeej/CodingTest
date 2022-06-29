def solution(record):
    answer = []
    
    # 아이디와 닉네임 매치시키기 위한 딕셔너리
    id_nick = {}
    # 들어감과 나감만 기록하기 위한 리스트
    order_list = []
    
    # 레코드 돌면서
    for rec_ in record:
        rec = rec_.split()
        # 입장일 경우 딕셔너리에 아이디와 닉네임 저장 후
        # 오더리스트에 Enter했음을 나타내는 1과 아이디 저장
        if rec[0] == "Enter":
            id_nick[rec[1]] = rec[2]
            order_list.append([1, rec[1]])
        # 닉네임 변경일 경우 딕셔너리에서 아이디 찾아서 닉네임만 변경
        elif rec[0] == "Change":
            id_nick[rec[1]] = rec[2]
        # 퇴장일 경우 오더리스트에 Leave했음을 나타내는 0과 아이디 저장
        else:
            order_list.append([0, rec[1]])
            
    # 오더리스트 돌면서 enter, leave 구별
    # 닉네임은 id_nick의 최종 결과에서 아이디를 기준으로 검색해서 가져옴
    for order in order_list:
        ans_str = f"{id_nick[order[1]]}님이 "
        if order[0] == 1:
            ans_str += "들어왔습니다."
        else:
            ans_str += "나갔습니다."
        answer.append(ans_str)
    
    
    return answer
