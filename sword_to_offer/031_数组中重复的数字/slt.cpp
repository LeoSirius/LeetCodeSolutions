class Solution{
public:
    bool duplicate(int numbers[], int length, int *duplication)
    {
        if (numbers == nullptr || length <= 0)
            return false;
        
        for (int i = 0; i < length; i++) {
            if (numbers[i] < 0 || numbers[i] > length - 1)
                return false;
        }

        for (int i = 0; i < length; i++) {
            while (numbers[i] != i) {
                if (numbers[i] == numbers[numbers[i]]) {
                    *duplication = numbers[i];
                    return true;
                }
                swap(numbers[i], numbers[numbers[i]]);
            }
        }
        return false;
    }
};