from typing import *
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        paths = defaultdict(list)
        for start, end in tickets:
            paths[start].append(end)
        for start in paths:
            paths[start].sort(reverse=True)   # 这里反转排序，因为后面加的时候是从尾部加的

        s = []
        # 这个dfs的从递归的底层开始添加元素的，所以最后返回的时候反转
        def search(start):
            while paths[start]:
                # 每次进递归，还是对当前“剩余可用目的地”循环，选择名字值小的进入下层时直接扣除这张机票
                search(paths[start].pop())
            s.append(start)

        search('JFK')
        return s[::-1]

def test(test_name, tickets, expected):
    res = Solution().findItinerary(tickets)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    expected1 = ["JFK", "MUC", "LHR", "SFO", "SJC"]
    test('test1', tickets1, expected1)

    tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    expected2 = ["JFK","ATL","JFK","SFO","ATL","SFO"]
    test('test2', tickets2, expected2)


# Given a list of airline tickets represented by pairs of departure and 
# arrival airports [from, to], reconstruct the itinerary in order. 
# All of the tickets belong to a man who departs from JFK. 
# Thus, the itinerary must begin with JFK.

# Note:

# If there are multiple valid itineraries, you should return the 
# itinerary that has the smallest lexical order when read as a single string. 
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order 
# than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# One must use all the tickets once and only once.

# Example 1:

# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

# Example 2:

# Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
#              But it is larger in lexical order.
