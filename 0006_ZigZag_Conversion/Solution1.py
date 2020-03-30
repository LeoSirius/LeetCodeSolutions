class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s

        str_list = ['' for i in range(numRows)]
        cur_row = 0
        for i in range(len(s)):
            str_list[cur_row] += s[i]
            if cur_row == 0:
                step = 1
            elif cur_row == numRows - 1:
                step = -1
            cur_row += step
        return ''.join(str_list)


def test(test_name, s, numRows, expected):
    res = Solution().convert(s, numRows)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')

if __name__ == "__main__":
    s1 = "PAYPALISHIRING"
    # P A H N
    # APLSIIG
    # Y I R
    numRows1 = 3
    expected1 = "PAHNAPLSIIGYIR"
    test("test1", s1, numRows1, expected1)

    s2 = "PAYPALISHIRING"
    numRows2 = 4
    expected2 = "PINALSIGYAHRPI"
    test("test2", s2, numRows2, expected2)

    s3 = "AB"
    numRows3 = 1
    expected3 = "AB"
    test("test3", s3, numRows3, expected3)