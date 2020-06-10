#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<double> twoSum(int n) {
        int dp[15][70];      // 根据n的范围1-11，70是够用的。j最大是n * 6，表示n次都是6
        memset(dp, 0, sizeof(dp));
        for (int j = 1; j <= 6; j++) {
            dp[1][j] = 1;
        }
        for (int i = 2; i <= n; i ++) {
            for (int j = i; j <= 6*i; j ++) {
                for (int cur = 1; cur <= 6; cur ++) {
                    if (j - cur <= 0) {
                        break;
                    }
                    dp[i][j] += dp[i-1][j-cur];
                }
            }
        }
        int all = pow(6, n);    // 所有可能情况的总数（包含重复的情况）
        vector<double> ret;
        // n个骰子，最小值是n，最大值是6 * n，一共 （6*n）- n + 1中可能的值（去掉重复）
        for (int i = n; i <= 6 * n; i ++) {
            ret.push_back((double)dp[n][i] / all);
        }
        return ret;
    }
};

bool is_vector_of_double_equal(vector<double> v1, vector<double> v2)
{
    if (v1.size() != v2.size())
        return false;
    for (int i = 0; i < v1.size(); i++) {
        if (0.00001 < abs(v1[i] - v2[i]))
            return false;
    }
    return true;
}

void test(string test_name, int n, vector<double> expected)
{
    vector<double> res = Solution().twoSum(n);
    if (is_vector_of_double_equal(res, expected))
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}


int main()
{
    int n1 = 1;
    vector<double> expected1 = {0.16667,0.16667,0.16667,0.16667,0.16667,0.16667};
    test("test1", n1, expected1);

    int n2 = 2;
    vector<double> expected2 = {0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778};
    test("test2", n2, expected2);

    return 0;
}

// 把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。

// 你需要用一个浮点数数组返回答案，
// 其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。

// 示例 1:
// 输入: 1
// 输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]

// 示例 2:
// 输入: 2
// 输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
//  

// 限制：
// 1 <= n <= 11
