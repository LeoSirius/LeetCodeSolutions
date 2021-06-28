from typing import *
from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        # 每个车站可以乘坐的公交车
        stations = defaultdict(set)
        for i, stops in enumerate(routes):
            for stop in stops:
                stations[stop].add(i)

        # 每个公交车要经过的车站
        routes = [set(x) for x in routes]

        q = deque([(source, 0)])

        buses = set()     # 已经做过的公交车
        stops = {source}  # 已经到达过的车站

        while q:
            pos, cost = q.popleft()
            if pos == target:
                return cost

            # 对于每个当前车站中尚未乘坐的 bus
            for bus in stations[pos] - buses:
                # 对上面那个 bus 能到的还没有去过的 stop
                for stop in routes[bus] - stops:
                    buses.add(bus)
                    stops.add(stop)
                    q.append((stop, cost+1))

        return -1


def test(test_name, routes, source, target, expected):
    res = Solution().numBusesToDestination(routes, source, target)
    if type(res) == type(expected) and res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    routes1 = [[1,2,7],[3,6,7]]
    source1 = 1
    target1 = 6
    expected1 = 2
    test('test1', routes1, source1, target1, expected1)

    routes2 = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
    source2 = 15
    target2 = 12
    expected2 = -1
    test('test2', routes2, source2, target2, expected2)
