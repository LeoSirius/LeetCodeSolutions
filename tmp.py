class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 or numRows >= len(s):
            return s
        
        strs = [''] * numRows
        step, idx = 1, 0

        for i in range(len(s)):
            strs[idx] += s[i]
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            idx += step
        return ''.join(strs)