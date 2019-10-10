class Solution{
public:
    bool Find(int *matrix, int rows, int columns, int target)
    {
        int row = 0;
        int col = columns - 1;
        while (row < rows && col >= 0) {
            if (target == matrix[row * columns + col]) {
                return true;
            } else if (target < matrix[row * columns + col]) {
                col--;
            } else {
                row++;
            }
        }
        return false;
    }
};