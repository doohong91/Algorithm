N = int(input())
nums = [int(input()) for _ in range(N)]

for i in range(len(nums)-1):
    for j in range(i, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

for n in nums:
    print(n)