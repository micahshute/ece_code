import random

nums = set()

while True:
    newnum = random.randint(1,10000)
    if newnum not in nums:
        nums.add(newnum)
    else:
        break

print(nums)
print(len(nums))
print(10000 ** 0.5)