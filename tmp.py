class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        idx, step = 0, 1
        res = [''] * numRows
        for i, v in enumerate(s):
            res[idx] += v
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        return ''.join(res)