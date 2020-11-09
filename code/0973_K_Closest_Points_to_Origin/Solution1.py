from typing import *

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        get_distance_square = lambda point : point[0] ** 2 + point[1] ** 2
        points.sort(key=get_distance_square)
        return points[:K]


def test(test_name, points, K, expected):
    res = Solution().kClosest(points, K)
    equal_tuple_cnt = 0
    for res_tuple in res:
        if res_tuple in expected:
            equal_tuple_cnt += 1
    
    if equal_tuple_cnt == len(expected) == len(res):
        print(f'{test_name} success.')
    else:
        print(f'{test_name} failed.')


if __name__ == "__main__":
    points1 = [[1,3],[-2,2]]
    K1 = 1
    expected1 = [[-2,2]]
    test('test1', points1, K1, expected1)

    points2 = [[3,3],[5,-1],[-2,4]]
    K2 = 2
    expected2 = [[3,3],[-2,4]]
    test('test2', points2, K2, expected2)


# We have a list of points on the plane. 
#  Find the K closest points to the origin (0, 0).

# (Here, the distance between two points on a plane is the Euclidean distance.)

# You may return the answer in any order. 
#  The answer is guaranteed to be unique (except for the order that it is in.)


# Example 1:

# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].


# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
 

# Note:

# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000