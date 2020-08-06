from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort()
        for i in range(len(citations)):
            h = len(citations) - i
            if citations[i] >= h:
                return h
        return 0


def test(test_name, citations, expected):
    res = Solution().hIndex(citations)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    citations1 = [3,0,6,1,5]
    expected1 = 3
    test('test1', citations1, expected1)

    citations2 = []
    expected2 = 0
    test('test2', citations2, expected2)

    citations3 = [0]
    expected3 = 0
    test('test3', citations3, expected3)

# Given an array of citations (each citation is a non-negative integer) of a
# researcher, write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: "A scientist
# has index h if h of his/her N papers have at least h citations each,
# and the other N − h papers have no more than h citations each."
#
# Example:

#
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
#              received 3, 0, 6, 1, 5 citations respectively.
#              Since the researcher has 3 papers with at least 3 citations each and the remaining
#              two with no more than 3 citations each, her h-index is 3.
# Note: If there are several possible values for h, the maximum one is taken as the h-index.
