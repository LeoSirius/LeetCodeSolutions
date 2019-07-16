### 思路1 利用3个二维数组一起检查

```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int used_row[9][9] = {0};
        int used_col[9][9] = {0};
        int used_square[9][9] = {0};
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[i].size(); j++){
                if(board[i][j] != '.'){
                    int num = board[i][j] - '0' - 1; // 下标是0-8
                    int k = i / 3 * 3 + j / 3;   // 把9个小方块分别归入0-8中
                    if(used_row[i][num] || used_col[j][num] || used_square[k][num]){
                        return false;
                    }
                    used_row[i][num] = used_col[j][num] = used_square[k][num] = 1;
                }
            }
        }
        return true;
    }
};
```

### 思路2 迭代分别检查行列和小正方形

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