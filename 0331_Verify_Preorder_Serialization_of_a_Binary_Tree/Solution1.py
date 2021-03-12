class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        diff = 1   # diff = 出度 - 入度。根节点没有入度，根节点1-1+2=2，正好是一开始的度数。
        nodes = preorder.split(',')

        for node in nodes:
            diff -= 1
            if diff < 0:
                return False
            if node != '#':
                diff += 2
        return diff == 0


def test(test_name, preorder, expected):
    res = Solution().isValidSerialization(preorder)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == '__main__':
    preorder1 = '9,3,4,#,#,1,#,#,2,#,6,#,#'
    expected1 = True
    test('test1', preorder1, expected1)

    preorder2 = '1,#'
    expected2 = False
    test('test2', preorder2, expected2)

    preorder3 = '9,#,#,1'
    expected3 = False
    test('test3', preorder3, expected3)

    preorder4 = '#,#,3,5,#'
    expected4 = False
    test('test4', preorder4, expected4)

