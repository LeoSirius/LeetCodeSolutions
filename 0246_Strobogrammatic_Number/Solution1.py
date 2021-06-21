class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        l, r = 0, len(num)-1
        mp = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        while l < r:
            if num[l] not in mp:
                return False
            if mp[num[l]] != num[r]:
                return False
            l += 1
            r -= 1
        return True if l > r else num[l] in ['0', '1', '8']


def test(test_name, num, expected):
    res = Solution().isStrobogrammatic(num)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == '__main__':
    num1 = '69'
    expected1 = True
    test('test1', num1, expected1)

    num2 = '88'
    expected2 = True
    test('test2', num2, expected2)

    num3 = '962'
    expected3 = False
    test('test3', num3, expected3)

    num4 = '1'
    expected4 = True
    test('test4', num4, expected4)
