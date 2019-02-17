N = int(input())
nums = sorted([int(input()) for _ in range(N)])

print(round(sum(nums)/len(nums)))
print(nums[len(nums)//2])
print(max(nums, key=nums.count))
print(max(nums) - min(nums))