class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        res = 0
        for i in range(1, len(num1) + 1):
            for j in range(1, len(num2) + 1):
                res += int(num1[-i]) * int(num2[-j]) * 10 ** (i+j-2)
        return str(res)

def test(test_name, num1, num2, expected):
    res = Solution().multiply(num1, num2)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    test("test1", '2', '3', '6')
    test('test2', '123', '456', '56088')
