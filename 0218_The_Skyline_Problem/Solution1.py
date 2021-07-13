from typing import *


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        pos_height = []
        for l, r, h in buildings:
            pos_height.append((l, -h))  # 用正负来标志是左边还是右边
            pos_height.append((r, h))
        pos_height.sort(key=lambda item: (item[0], item[1]))

        cur_handle = [0]
        pre_max_h, cur_max_h = 0, 0

        res = []
        for pos, h in pos_height:
            # 左边时，把高度加进去。到右边了，把高度 remove
            if h < 0:
                cur_handle.append(-h)
            else:
                cur_handle.remove(h)
            cur_max_h = max(cur_handle)
            if pre_max_h != cur_max_h:
                res.append([pos, cur_max_h])
                pre_max_h = cur_max_h
        return res


def test(test_name, buildings, expected):
    res = Solution().getSkyline(buildings)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    buildings1 = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
    expected1 = [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    test('test1', buildings1, expected1)

    buildings2 = [[0,2,3],[2,5,3]]
    expected2 = [[0,3],[5,0]]
    test('test2', buildings2, expected2)
