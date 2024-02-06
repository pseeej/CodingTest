import sys
input = sys.stdin.readline

tmp = input().strip()
while tmp != "end":
    board = []
    line = []
    for i in range(len(tmp)):
        if i != 0 and i%3 == 0:
            board.append(line)
            line = []
        line.append(tmp[i])
    board.append(line)

    xcnt = tmp.count('X')
    ocnt = tmp.count('O')

    bingchk = [set() for _ in range(8)]
    for i in range(3):
        bingchk[0].add(board[i][0])
        bingchk[1].add(board[i][1])
        bingchk[2].add(board[i][2])

        bingchk[3].add(board[0][i])
        bingchk[4].add(board[1][i])
        bingchk[5].add(board[2][i])

        bingchk[6].add(board[i][i])
        bingchk[7].add(board[2-i][i])

    # print(bingchk)

    checkIfPossible = False
    bings = set()
    for bing in bingchk:
        if len(bing) == 1 and list(bing)[0] == 'X':
            bings.add(list(bing)[0])
        if len(bing) == 1 and list(bing)[0] == 'O':
            bings.add(list(bing)[0])

    # print(bings)

    if len(bings) == 1 and ((list(bings)[0] == 'X' and xcnt == ocnt+1) or (list(bings)[0] == 'O' and xcnt == ocnt)):
        print("valid")
    elif len(bings) == 0 and tmp.count('.') == 0 and xcnt == ocnt + 1:
        print("valid")
    # elif not checkIfPossible and tmp.count('.') == 0 and bing == 'X' and xcnt == ocnt+1:
        # print("valid")
    else:
        print("invalid")
        

    tmp = input().strip()

    
