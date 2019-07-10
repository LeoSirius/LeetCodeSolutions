### 思路1 迭代分别检查行列和小正方形

```python
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.is_unit_valid(row):
                return False

        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False

        # 把一个3*3的小正方形存入一个list中，再检查
        for i in (0,3,6):
            for j in (0,3,6):
                square = [board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
                if not self.is_unit_valid(square):
                    return False

        return True

    # 对每一个输入的list，首先去除点，然后检查数字有没有重复
    def is_unit_valid(self, nums):
        nums = [i for i in nums if i != '.']
        return len(nums) == len(set(nums))
```