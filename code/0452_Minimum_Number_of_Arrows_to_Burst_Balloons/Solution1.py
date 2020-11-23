from typing import *

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda item: item[1])
        res = 0
        
        tail = -float('inf')
        for point in points:
            if tail < point[0]:
                tail = point[1]
                res += 1
        return res



def test(test_name, points, expected):
    res = Solution().findMinArrowShots(points)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    points1 = [[10,16],[2,8],[1,6],[7,12]]
    expected1 = 2
    test('test1', points1, expected1)

    points2 = [[1,2],[3,4],[5,6],[7,8]]
    expected2 = 4
    test('test2', points2, expected2)

    points3 = [[1,2],[2,3],[3,4],[4,5]]
    expected3 = 2
    test('test3', points3, expected3)

    points4 = [[1,2]]
    expected4 = 1
    test('test4', points4, expected4)

    points5 = [[2,3],[2,3]]
    expected5 = 1
    test('test5', points5, expected5)

    points6 = [[1,2],[2,3],[3,4],[4,5]]
    expected6 = 2
    test('test6', points6, expected6)

    points7 = [[-2147483648,2147483647]]
    expected7 = 1
    test('test7', points7, expected7)

    points8 = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    expected8 = 2
    test('test8', points8, expected8)



# There are some spherical balloons spread in two-dimensional space. 
# For each balloon, provided input is the start and end coordinates of 
# the horizontal diameter. Since it's horizontal, y-coordinates don't matter,
#  and hence the x-coordinates of start and end of the diameter suffice. 
#  The start is always smaller than the end.

# An arrow can be shot up exactly vertically from different points along the x-axis. 
# A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend.
#  There is no limit to the number of arrows that can be shot. 
#  An arrow once shot keeps traveling up infinitely.

# Given an array points where points[i] = [xstart, xend], 
# return the minimum number of arrows that must be shot to burst all balloons.

#  

# Example 1:

# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).

# Example 2:

# Input: points = [[1,2],[3,4],[5,6],[7,8]]
# Output: 4

# Example 3:

# Input: points = [[1,2],[2,3],[3,4],[4,5]]
# Output: 2

# Example 4:

# Input: points = [[1,2]]
# Output: 1

# Example 5:

# Input: points = [[2,3],[2,3]]
# Output: 1
#  

# Constraints:

# 0 <= points.length <= 104
# points[i].length == 2
# -231 <= xstart < xend <= 231 - 1

