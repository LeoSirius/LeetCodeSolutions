#include <iostream>
using namespace std;

class Solution {
public:
    int numWays(int n) {
        int last2 = 1, last1 = 1;
        if (n == 0 || n == 1)
            return last1;
        for (int i = 2; i <= n; i++) {
            int tmp = last1;
            last1 = (last1 + last2) % 1000000007;
            last2 = tmp;
        }
        return last1;
    }
};
// 1000000007

void test(string test_name, int n, int expected)
{
    int res = Solution().numWays(n);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int n1 = 2;
    int expected1 = 2;
    test("test1", n1, expected1);

    int n2 = 7;
    int expected2 = 21;
    test("test2", n2, expected2);

    int n3 = 0;
    int expected3 = 1;
    test("test3", n3, expected3);
}


// 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

// 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

// 示例 1：

// 输入：n = 2
// 输出：2
// 示例 2：

// 输入：n = 7
// 输出：21
// 示例 3：

// 输入：n = 0
// 输出：1
// 提示：

// 0 <= n <= 100
