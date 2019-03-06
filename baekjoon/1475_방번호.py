room = input()
nums = [0]*9
cnt = 1
for i in range(len(room)):
    if int(room[i]) == 6 or int(room[i]) == 9:
        nums[6] += 0.5
        if nums[6] > cnt:
            cnt += 1
    else:
        nums[int(nums[i])] += 1
        if nums[int(nums[i])] > cnt:
            cnt += 1
print(cnt)