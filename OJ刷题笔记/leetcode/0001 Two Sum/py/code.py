from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buff_dict = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in buff_dict:
                return [buff_dict[m], i]
            else:
                buff_dict[n] = i


# test code
s = Solution()

def test_func(nums, target, expected):
    result = s.twoSum(nums, target)
    if result == expected:
        return True
    else:
        return False

def test1():
    if (test_func([2, 7, 11, 15], 9, [0, 1])):
        print('test 1 success')
    else:
        print('test 1 failed')

def do_test():
    test1()  
do_test()  

