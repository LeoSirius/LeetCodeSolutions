from typing import *


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()

        res = []
        for query in queries:
            # print(f'query = {query}')
            if query[1] < nums[0]:
                res.append(-1)
                continue

            cur = query[0] ^ nums[0]
            for n in nums:
                if n > query[1]:
                    break
                # print(f'query[0] ^ n = {query[0] ^ n}')
                cur = max(cur, query[0] ^ n)
            res.append(cur)



        return res



def test(test_name, nums, queries, expected):
    res = Solution().maximizeXor(nums, queries)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    nums1 = [0,1,2,3,4]
    queries1 = [[3,1],[1,3],[5,6]]
    expected1 = [3,3,7]
    test('test1', nums1, queries1, expected1)

    nums2 = [5,2,4,6,6,3]
    queries2 = [[12,4],[8,1],[6,3]]
    expected2 = [15,-1,5]
    test('test2', nums2, queries2, expected2)
