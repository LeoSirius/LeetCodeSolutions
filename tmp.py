class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            num_to_find = target - nums[i]
            if num_to_find in my_dict.keys():
                return [my_dict[num_to_find], i]
            my_dict[nums[i]] = i