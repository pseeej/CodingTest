import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    susiks = []
    def DFS(susik, currnum):
        global susiks
        
        if currnum > N:
            susiks.append(susik)
            return

        newsusik = susik + " " + str(currnum)
        DFS(newsusik, currnum+1)

        newsusik = susik + "+" + str(currnum)
        DFS(newsusik, currnum+1)

        newsusik = susik + "-" + str(currnum)
        DFS(newsusik, currnum+1)

    DFS("1", 2)
    susiks.sort()


    for susik in susiks:
        num = ""
        result = 0
        for i in range(len(susik)-1, -1, -1):
            if "1" <= susik[i] <= "9":
                num = susik[i] + num
            elif susik[i] == " ":
                pass
            elif susik[i] == "+":
                result += int(num)
                num = ""
            elif susik[i] == "-":
                result -= int(num)
                num = ""

        result += int(num)
        # print(result, susik)


        if result == 0:
            print(susik)

    print()
