def test_binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        print(f'l = {l}, r = {r}, mid = {mid}')
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1

res = test_binary_search([1,2,3,4,5,6,7,8,9,10], 6)
print(res)