from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs:
            return 0
        house_num = len(costs)
        dp = [[0 for i in range(3)] for i in range(house_num)]
        dp[0] = costs[0]

        for i in range(1, house_num):
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        return min(dp[-1][0], dp[-1][1], dp[-1][2])

def test(test_name, costs, expected):
    res = Solution().minCost(costs)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    costs1 = [[17,2,17],[16,16,5],[14,3,19]]
    expected1 = 10
    test('test1', costs1, expected1)

    costs2 = []
    expected2 = 0
    test('test2', costs2, expected2)
