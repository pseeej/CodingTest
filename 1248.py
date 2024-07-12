import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
signs = list(input().strip())

linelimit = N
signboard = []
idx = 0

tmpline = []
linecnt = 0
while idx < len(signs):
    tmpline.append(signs[idx])
    idx += 1
    linecnt += 1

    if linecnt == linelimit:
        linecnt = 0
        linelimit -= 1
        signboard.append(tmpline)
        tmpline = []


def findNextNumber(currseq, curridx):
    possnums = {i for i in range(-10, 11)}

    for i in range(curridx+1):
        currsum = 0
        for j in range(curridx+1-i):
            currsum += currseq[j+i]

            if signboard[i][j] == "+" and currsum > 0:
                pass
            elif signboard[i][j] == "-" and currsum < 0:
                pass
            elif signboard[i][j] == "0" and currsum == 0:
                pass
            else:
                return

        if curridx-i+1 < N-i:
            if signboard[i][curridx-i+1] == "+":
                for j in range(-10, -currsum+1):
                    possnums.discard(j)
            elif signboard[i][curridx-i+1] == "-":
                for j in range(-currsum, 11):
                    possnums.discard(j)
            elif signboard[i][curridx-i+1] == "0" and -10 <= currsum <= 10:
                possnums = {-currsum}
            else:
                return

        # print(currseq, currsum, possnums)
            

    if len(currseq) == N:
        print(' '.join(map(str, currseq)))
        exit()

    if signboard[curridx+1][0] == "+":
        for i in range(-10, 0):
            possnums.discard(i)
    elif signboard[curridx+1][0] == "-":
        for i in range(1, 11):
            possnums.discard(i)
    elif signboard[curridx+1][0] == "0":
        possnums = {0}
    
    for num in possnums:
        currseq.append(num)
        findNextNumber(currseq, curridx+1)
        currseq.pop()
    

    

for i in range(-10, 11):
    findNextNumber([i], 0)
