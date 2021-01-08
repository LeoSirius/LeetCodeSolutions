from typing import *

class UnionFind:
    def __init__(self) -> None:
        self.father = {}
        self.num_of_sets = 0
    
    def find(self,x):
        root = x
        
        # 必须用None判断，因为可能是0
        while self.father[root] != None:
            root = self.father[root]
        
        # 路径压缩
        while x != root:
            old_father = self.father[x]
            self.father[x] = root
            x = old_father
        
        return root


    def merge(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            self.father[rootx] = rooty
            self.num_of_sets -= 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def add(self, x):
        if x not in self.father:
            self.father[x] = None
            self.num_of_sets += 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind()
        for i in range(len(isConnected)):
            uf.add(i)
            for j in range(i):
                if isConnected[i][j]:
                    uf.merge(i, j)
        
        return uf.num_of_sets


def test(test_name, isConnected, expected):
    res = Solution().findCircleNum(isConnected)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    isConnected1 = [
        [1,1,0],
        [1,1,0],
        [0,0,1]]
    expected1 = 2
    test('test1', isConnected1, expected1)

    isConnected2 = [
        [1,0,0],
        [0,1,0],
        [0,0,1]]
    expected2 = 3
    test('test2', isConnected2, expected2)

    isConnected3 = [
        [1,1,1],
        [1,1,1],
        [1,1,1]]
    expected3 = 1
    test('test3', isConnected3, expected3)



# There are n cities. Some of them are connected, while some are not. 
# If city a is connected directly with city b, and city b is connected 
# directly with city c, then city a is connected indirectly with city c.

# A province is a group of directly or indirectly connected cities and 
# no other cities outside of the group.

# You are given an n x n matrix isConnected where isConnected[i][j] = 1 
# if the ith city and the jth city are directly connected, 
# and isConnected[i][j] = 0 otherwise.

# Return the total number of provinces.


# Constraints:

# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]


