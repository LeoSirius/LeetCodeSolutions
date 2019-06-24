class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows == 1:
            return s
        step = 1
        index = 0
        res = [''] * numRows
        for i, v in enumerate(s):
            # cur_line is not index
            res[index] += v
            if index == numRows-1:
                step = -1
            elif index == 0:
                step = 1
            index += step
        return ''.join(res)

s = Solution()
t = s.convert('PAYPALISHIRING', 3)
print(t)