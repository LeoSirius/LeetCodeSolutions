from typing import *


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:

        # 把所有的item放都放到group里面，如果item的group_id是-1，则用模拟的group_id
        group_id = m
        for i in range(len(group)):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
        
        # indegree_g和graph_g记录组之间的顺序
        # indegree_i和graph_i记录元素之间的顺序
        indegree_g = [0 for _ in range(group_id)]
        indegree_i = [0 for _ in range(n)]
        vector_g = [set() for _ in range(group_id)]
        graph_g = [set() for _ in range(group_id)]
        graph_i = [set() for _ in range(n)]

        # vector_g的索引是群组id，value是这个群组里的item集合
        for i in range(len(group)):
            vector_g[group[i]].add(i)

        # 构造小组的依赖关系和组内项目的依赖关系。
        for i in range(len(beforeItems)):
            for item in beforeItems[i]:
                # 如果i所在的群组等于item所在的群组
                # 则记录组内元素之间的关系
                if group[i] == group[item]:
                    indegree_i[i] += 1
                    graph_i[item].add(i)
                else:
                    # 否则，如果当前元素所在的群组（group[i]）不和item的群组（group[item]）相连
                    # 那么则记录组之间的关系
                    if group[i] not in graph_g[group[item]]:
                        indegree_g[group[i]] += 1
                        graph_g[group[item]].add(group[i])
        
        #group top sort
        qu = []
        orderG = []
        for i in range(group_id):
            if indegree_g[i] == 0:
                qu.append(i)
        if len(qu) == 0:
            return []
        
        while len(qu) > 0:
            t = []
            while len(qu) > 0:
                curr = qu.pop()
                print(curr)
                orderG.append(curr)
                
                for neg in graph_g[curr]:
                    indegree_g[neg] -= 1
                    if indegree_g[neg] == 0:
                        t.append(neg)
            qu = t
        
        if len(orderG) != group_id:
            return []
        
        #items top sort
        res = []
        for i in range(len(orderG)):
            
            qu = []
            for item in vector_g[orderG[i]]:
                if indegree_i[item] == 0:
                    qu.append(item)
            
            count = 0
            while len(qu) > 0:
                t = []
                while len(qu) > 0:
                    curr = qu.pop()
                    res.append(curr)
                    count += 1
                    
                    for neg in graph_i[curr]:
                        indegree_i[neg] -= 1
                        if indegree_i[neg] == 0:
                            t.append(neg)
                qu = t
            
            if count != len(vector_g[orderG[i]]):
                return []
        
        return res



def test(test_name, n, m, group, beforeItems, expected_arr):
    res = Solution().sortItems(n, m, group, beforeItems)
    print(f'res = {res}')
    if res in expected_arr:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1, m1 = 8, 2
    group1 = [-1,-1,1,0,0,1,0,-1]
    beforeItems1 = [[],[6],[5],[6],[3,6],[],[],[]]
    expected_arr1 = [[6,3,4,1,5,2,0,7],  [7, 0, 5, 2, 6, 3, 4, 1]]
    test('test1', n1, m1, group1, beforeItems1, expected_arr1)

    n2, m2 = 8, 2
    group2 = [-1,-1,1,0,0,1,0,-1]
    beforeItems2 = [[],[6],[5],[6],[3],[],[4],[]]
    expected_arr2 = [[]]
    test('test2', n2, m2, group2, beforeItems2, expected_arr2)


# There are n items each belonging to zero or one of m groups where group[i]
#  is the group that the i-th item belongs to and it's equal to -1 if 
# the i-th item belongs to no group. The items and the groups are zero indexed. 
# A group can have no item belonging to it.

# Return a sorted list of the items such that:

# The items that belong to the same group are next to each other in the sorted list.
# There are some relations between these items where beforeItems[i] is a list 
# containing all the items that should come before the i-th item in the sorted
#  array (to the left of the i-th item).
# Return any solution if there is more than one solution and return an empty 
# list if there is no solution.


