from typing import *

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        for i in range(2, n):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        return min(cost[-1], cost[-2])


def test(test_name, cost, expected):
    res = Solution().minCostClimbingStairs(cost)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    cost1 = [10, 15, 20]
    expected1 = 15
    test('test1', cost1, expected1)

    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    expected2 = 6
    test('test2', cost2, expected2)



# On a staircase, the i-th step has some non-negative cost cost[i]
#  assigned (0 indexed).

# Once you pay the cost, you can either climb one or two steps. 
# You need to find minimum cost to reach the top of the floor,
#  and you can either start from the step with index 0, or the step with index 1.

# Example 1:
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

# Example 2:
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

# Note:
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].

