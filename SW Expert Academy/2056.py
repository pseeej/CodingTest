T = int(input())
for test_case in range(1, T + 1):
    date = input()
    if len(date) != 8:
        print(f"#{test_case} -1")

    year = date[:4]
    month = date[4:6]
    day = date[6:]

    if int(month) in {1, 3, 5, 7, 8, 10, 12} and 1 <= int(day) <= 31:
        print(f"#{test_case} {year}/{month}/{day}")
    elif int(month) in {4, 6, 9, 11} and 1 <= int(day) <= 30:
        print(f"#{test_case} {year}/{month}/{day}")
    elif int(month) == 2 and 1 <= int(day) <= 28:
        print(f"#{test_case} {year}/{month}/{day}")
    else:
        print(f"#{test_case} -1")
