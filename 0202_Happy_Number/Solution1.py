class Solution:
    def isHappy(self, n: int) -> bool:
        def process(x):
            res = 0
            while x:
                digit = x % 10
                x //= 10
                res += digit * digit
            return res

        slow = process(n)
        fast = process(slow)

        while fast != slow:
            fast = process(process(fast))
            slow = process(slow)
        return fast == 1


def test(test_name, n, expected):
    res = Solution().isHappy(n)
    if res == expected:
        print(test_name + ' succeed')
    else:
        print(test_name + ' fail')


if __name__ == "__main__":
    n1 = 19
    expected1 = True
    test('test1', n1, expected1)

    n2 = 1
    expected2 = True
    test('test2', n2, expected2)

    n3 = 7
    expected3 = True
    test('test3', n3, expected3)

    n4 = 2
    expected4 = False
    test('test4', n4, expected4)

