class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buff_dict = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in buff_dict:
                return [buff_dict[m], i]
            else:
                buff_dict[n] = i