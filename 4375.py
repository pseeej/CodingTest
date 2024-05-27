while True:
    try:
        num = int(input())
        newnum = "1"
        pluss = "1"

        while int(newnum) % num != 0:
            newnum += pluss

        print(len(newnum))
    except:
        break
    
