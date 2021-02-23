from typing import *


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        l, r = 0, 0

        satisfied_count, unsatisfied_count = 0, 0
        max_unsatisfied = 0

        while r < len(customers):
            if grumpy[r]:
                unsatisfied_count += customers[r]
            else:
                satisfied_count += customers[r]

            if r + 1 - l > X:
                if grumpy[l]:
                    unsatisfied_count -= customers[l]
                l += 1

            max_unsatisfied = max(max_unsatisfied, unsatisfied_count)
            r += 1

        return satisfied_count + max_unsatisfied



def test(test_name, customers, grumpy, X, expected):
    res = Solution().maxSatisfied(customers, grumpy, X)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    customers1 = [1,0,1,2,1,1,7,5]
    grumpy1    = [0,1,0,1,0,1,0,1]
    X1 = 3
    expected1 = 16
    test('test1', customers1, grumpy1, X1, expected1)

