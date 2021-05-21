class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        
        last_say = self.countAndSay(n-1)
        new_say = ''
        cnt = 1

        for i in range(1, len(last_say)):
            if last_say[i] == last_say[i-1]:
                cnt += 1
            else:
                new_say += str(cnt) + last_say[i-1]
                cnt = 1
        new_say += str(cnt) + last_say[-1]
        return new_say


def test(test_name, n, expected):
    res = Solution().countAndSay(n)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    n1 = 1
    expected1 = "1"
    test("test1", n1, expected1)
        
    n2 = 4
    expected2 = "1211"
    test("test2", n2, expected2)
        
    n3 = 6
    expected3 = "312211"
    test("test3", n3, expected3)