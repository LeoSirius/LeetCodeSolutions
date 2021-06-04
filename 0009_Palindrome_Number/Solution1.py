class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x % 10 == 0:
            return False

        mirror = 0
        while mirror < x:
            digit = x % 10
            x //= 10
            mirror = mirror * 10 + digit

        return mirror == x or mirror // 10 == x


def test(test_name, x, expected):
    res = Solution().isPalindrome(x)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    test('test1', 121, True)
    test('test2', -121, False)
    test('test3', 10, False)
