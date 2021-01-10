from typing import *

class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for i in range(0, len(encoded)):
            arr.append(encoded[i]^arr[i])
        return arr


def test(test_name, encoded, first, expected):
    res = Solution().decode(encoded, first)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    encoded1 = [1,2,3]
    first1 = 1
    expected1 = [1,0,2,1]
    test('test1', encoded1, first1, expected1)

    encoded2 = [6,2,7,3]
    first2 = 4
    expected2 = [4,2,0,7,4]
    test('test2', encoded2, first2, expected2)
