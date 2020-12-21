from typing import *
import functools


def cmp_pair(a, b):
    if a[0] == b[0]:
        return a[1] - b[1]
    return b[0] - a[0]


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=functools.cmp_to_key(cmp_pair))
        res = []
        for pair in people:
            res.insert(pair[1], pair)
        return res


def test(test_name, people, expected):
    res = Solution().reconstructQueue(people)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    people1 = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    expected1 = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
    test('test1', people1, expected1)


# Suppose you have a random list of people standing in a queue. 
# Each person is described by a pair of integers (h, k), where h is 
# the height of the person and k is the number of people in front of 
# this person who have a height greater than or equal to h. 
# Write an algorithm to reconstruct the queue.

# Note:
# The number of people is less than 1,100.

# Example

# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

