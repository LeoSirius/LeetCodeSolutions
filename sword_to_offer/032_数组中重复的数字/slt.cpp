class Solution{
public:
int countRange(const int *numbers, int length, int start, int end)
{
    if (numbers == nullptr)
        return false;
    int count = 0;
    for (int i = 0; i < length; i++) {
        if (numbers[i] >= start && numbers[i] <= end)
            count++;
    }
    return count;
}

int getDuplication(const int* numbers, int length)
{
    if (numbers == nullptr || length <= 0)
        return -1;
    
    // 注意start和end不是索引，而是数组中的1~n的值
    int start = 1;
    int end = length - 1;
    while (end >= start) {
        int middle = (end - start) / 2 + start;
        int count = countRange(numbers, length, start, middle);
        if (end == start) {
            if (count > 1)      // 数值区间中只有一个数，且这个数出现了不止一次
                return start;
            break;
        }

        if (count > (middle - start + 1)) {
            end = middle;
        } else {
            start = middle + 1;
        }
    }
    return -1;
}
};