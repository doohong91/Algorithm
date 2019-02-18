N = int(input())
nums = [0]*N
counts = [0]*8001
for i in range(N):
    n = int(input())
    nums[i] = n
    counts[n] += 1
nums = sorted(nums)
print(round(sum(nums)/len(nums)))
print(nums[len(nums)//2])
mode = counts.index(max(counts))
print(mode-8000 if mode > 4000 else mode)
print(max(nums) - min(nums))