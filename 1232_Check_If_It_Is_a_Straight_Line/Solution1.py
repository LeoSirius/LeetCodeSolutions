from typing import *

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True

        x0 = coordinates[1][0]-coordinates[0][0]
        y0 = coordinates[1][1]-coordinates[0][1]
        for i in range(2, len(coordinates)):
            xi = coordinates[i][0]-coordinates[i-1][0]
            yi = coordinates[i][1]-coordinates[i-1][1]
            
            if yi * x0 != y0 * xi:
                return False

        return True


def test(test_name, coordinates, expected):
    res = Solution().checkStraightLine(coordinates)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    coordinates1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    expected1 = True
    test('test1', coordinates1, expected1)

    coordinates2 = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    expected2 = False
    test('test2', coordinates2, expected2)

    coordinate3 = [[0,0],[0,1],[0,-1]]
    expected3 = True
    test('test3', coordinate3, expected3)

    coordinate4 = [[1,1],[2,2],[2,0]]
    expected4 = False
    test('test4', coordinate4, expected4)


# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] 
# represents the coordinate of a point. Check if these points make a straight 
# line in the XY plane.


# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true

# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false


# Constraints:

# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.
