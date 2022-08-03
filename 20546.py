money = int(input())
prices = list(map(int, input().split()))

# BNP
jh_money = money
jh_asset = 0
for i in range(14-1):
    if prices[i] <= jh_money:
        amount = jh_money // prices[i]
        jh_asset += amount
        jh_money -= amount*prices[i]

# TIMING
sm_money = money
sm_asset = 0
inc = 0
dec = 0
for i in range(1, 14-1):
    prev_price = prices[i-1]
    now_price = prices[i]

    if prev_price > now_price:
        dec += 1
        inc = 0
    if prev_price < now_price:
        inc += 1
        dec = 0

    if inc >= 3:
        sm_money += now_price * sm_asset
        sm_asset = 0

    if dec >= 3:
        amount = sm_money // now_price
        sm_money -= amount * now_price
        sm_asset += amount


bnp = jh_money + jh_asset * prices[13]
timing = sm_money + sm_asset * prices[13]

if bnp>timing:
    print("BNP")
elif bnp < timing:
    print("TIMING")
else:
    print("SAMESAME")
