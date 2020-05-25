#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int minArray(vector<int>& numbers) {
        int l = 0, r = numbers.size() - 1;
        int mid;
        while (l < r) {
            mid = l + (r - l) / 2;
            // 最小数pivot <= mid
            if (numbers[mid] < numbers[r])
                r = mid;
            // 最小数pivot > mid
            else if (numbers[r] < numbers[mid])
                l = mid + 1;
            // 去重[mid, r]都是相等的
            else
                r--;
        }
        return numbers[l];
    }
};


void test(string test_name, vector<int> numbers, int expected)
{
    int res = Solution().minArray(numbers);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> numbers1 = {3,4,5,1,2};
    int expected1 = 1;
    test("test1", numbers1, expected1);

    vector<int> numbers2 = {2,2,2,0,1};
    int expected2 = 0;
    test("test2", numbers2, expected2);

    return 0;
}


// 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
// 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
// 例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

