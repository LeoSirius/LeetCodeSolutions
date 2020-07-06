from typing import *

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        # 初始化入度数组和邻接表
        in_degrees = [0 for _ in range(numCourses)]
        # 注意set必须这样初始化，
        # 如果 adj = [set()] * numCourses，
        # 那么set元素的相同的引用
        adj = [set() for _ in range(numCourses)]

        for end, start in prerequisites:
            in_degrees[end] += 1
            adj[start].add(end)

        # 先把入度为0的节点号加到que中
        que = []
        for i in range(numCourses):
            if in_degrees[i] == 0:
                que.append(i)

        cnt = 0  # 用来表示已经学习的课程的数量
        while que:
            cur_node = que.pop(0)
            cnt += 1

            for successor in adj[cur_node]:
                in_degrees[successor] -= 1
                if in_degrees[successor] == 0:
                    que.append(successor)

        return cnt == numCourses


def test(test_name, numCourses, prerequisites, expected):
    res = Solution().canFinish(numCourses, prerequisites)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    numCourses1 = 2
    prerequisites1 = [[1,0]]
    expected1 = True
    # test('test1', numCourses1, prerequisites1, expected1)

    numCourses2 = 2
    prerequisites2 = [[1,0],[0,1]]
    expected2 = False
    # test('test2', numCourses2, prerequisites2, expected2)

    numCourses3 = 3
    prerequisites3 = [[1,0],[1,2],[0,1]]
    expected3 = False
    test('test3', numCourses3, prerequisites3, expected3)



# There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
#
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
# which is expressed as a pair: [0,1]
#
# Given the total number of courses and a list of prerequisite pairs,
# is it possible for you to finish all courses?
#
#  
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
#              To take course 1 you should have finished course 0, and to take course 0 you should
#              also have finished course 1. So it is impossible.
#  
#
# Constraints:
#
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 1 <= numCourses <= 10^5
