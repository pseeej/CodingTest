a = input()
b = input()
c = input()

res = int(a) * int(b) * int(c)

res = str(res)

nums = [0 for _ in range(10)]

for i in res:
    nums[int(i)]+=1

for i in range(10):
    print(nums[i])