from typing import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]

        in_degrees = [0 for _ in range(numCourses)]
        adj = [set() for _ in range(numCourses)]

        for end, start in prerequisites:
            in_degrees[end] += 1
            adj[start].add(end)

        que = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                que.append(i)

        res = []
        cnt = 0
        while que:
            cur_node = que.pop(0)
            cnt += 1
            res.append(cur_node)

            for successor in adj[cur_node]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    que.append(successor)

        return res if cnt == numCourses else []

def test(test_name, numCourses, prerequisites, expecteds):
    res = Solution().findOrder(numCourses, prerequisites)
    if res in expecteds:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == '__main__':
    numCourses1 = 2
    prerequisites1 = [[1,0]]
    expected1 = [[0,1]]
    test('test1', numCourses1, prerequisites1, expected1)

    numCourses2 = 4
    prerequisites2 = [[1,0],[2,0],[3,1],[3,2]]
    expected2 = [[0,1,2,3], [0,2,1,3]]
    test('test2', numCourses2, prerequisites2, expected2)

    numCourses3 = 1
    prerequisites3 = []
    expected3 = [[0]]
    test('test3', numCourses3, prerequisites3, expected3)

#
# There are a total of n courses you have to take, labeled from 0 to n-1.
#
# Some courses may have prerequisites, for example to take course 0
# you have to first take course 1, which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs,
# return the ordering of courses you should take to finish all courses.
#
# There may be multiple correct orders, you just need to return one of them.
# If it is impossible to finish all courses, return an empty array.


# Input: 2, [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
#              course 0. So the correct course order is [0,1] .
# Example 2:
#
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
#              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
#              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
