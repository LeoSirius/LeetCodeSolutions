class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: nums' element, value: index of that element
        mapping = {}
        for i in range(len(nums)):
            num_to_find = target - nums[i]
            if num_to_find in mapping.keys():
                return [i, mapping[num_to_find]]
            else:
                mapping[nums[i]] = i
