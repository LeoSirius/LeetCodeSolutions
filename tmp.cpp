class Solution{
public:
// 参数:
//        numbers:     一个整数数组
//        length:      数组的长度
// 返回值:             
//        duplication: (输出) 数组中的一个重复的数字, 没有则返回-1
    int duplicate(int numbers[], int length)
    {
        for (int i = 0; i < length; i++) {
            while (numbers[i] != i) {
                if (numbers[i] == numbers[numbers[i]]) {
                    return numbers[i];
                }
                swap(numbers[i], numbers[numbers[i]]);
            }
        }
        return -1;
    }
};