def find_small_index(nums):
    l, r = 0, len(nums) - 1

    while l < r:
        m = (l+r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    print(f'l = {l}, m = {m}, r = {r}')
    return l

nums = [4,5,6,7,8,9,1,2]
res = find_small_index(nums)
print(res)