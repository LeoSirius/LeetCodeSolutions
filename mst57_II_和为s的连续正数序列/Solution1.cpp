#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> findContinuousSequence(int target) {
        vector<vector<int>> res;
        int sum = 0;
        int l = 1, r = 1;

        // 注意[l,r)左闭右开
        while (l <= target / 2) {
            if (sum == target) {
                vector<int> row;
                for (int i = l; i < r; i++)
                    row.push_back(i);
                res.push_back(row);
                sum -= l;
                l++;
            } else if (sum < target) {
                sum += r;
                r++;
            } else {
                sum -= l;
                l++;
            }
        }
        return res;
    }
};

void test(string test_name, int target, vector<vector<int>> expected)
{
    vector<vector<int>> res = Solution().findContinuousSequence(target);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int target1 = 9;
    vector<vector<int>> expected1 = {{2,3,4}, {4,5}};
    test("test1", target1, expected1);

    int target2 = 15;
    vector<vector<int>> expected2 = {{1,2,3,4,5}, {4,5,6}, {7,8}};
    test("test2", target2, expected2);

    return 0;
}

// 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
// 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

// 示例 1：
// 输入：target = 9
// 输出：[[2,3,4],[4,5]]

// 示例 2：
// 输入：target = 15
// 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
//  

// 限制：
// 1 <= target <= 10^5

