#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getLeastNumbers(vector<int>& arr, int k) {
        sort(arr.begin(), arr.end());
        return vector<int>(arr.begin(), arr.begin() + k);
    }
};

void test(string test_name, vector<int> arr, int k, vector<int> expected)
{
    vector<int> res = Solution().getLeastNumbers(arr, k);
    sort(res.begin(), res.end());
    sort(expected.begin(), expected.end());
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> arr1 = {3,2,1};
    int k1 = 2;
    vector<int> expected1 = {1,2};
    test("test1", arr1, k1, expected1);

    vector<int> arr2 = {0,1,2,1};
    int k2 = 1;
    vector<int> expected2 = {0};
    test("test2", arr2, k2, expected2);

    return 0;
}

// 输入整数数组 arr ，找出其中最小的 k 个数。例如，
// 输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。


// 示例 1：
// 输入：arr = [3,2,1], k = 2
// 输出：[1,2] 或者 [2,1]

// 示例 2：
// 输入：arr = [0,1,2,1], k = 1
// 输出：[0]
//  

// 限制：
// 0 <= k <= arr.length <= 10000
// 0 <= arr[i] <= 10000
