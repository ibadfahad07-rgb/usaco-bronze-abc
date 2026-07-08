nums = list(map(int, input().split()))

nums.sort()

a = nums[0]
b = nums[1]
c = nums[6]-a-b

print(a, b, c)