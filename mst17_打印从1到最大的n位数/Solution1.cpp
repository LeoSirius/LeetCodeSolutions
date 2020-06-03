#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<int> printNumbers(int n) {
        vector<int> res;
        int max = pow(10, n) - 1;
        for (int i = 1; i <= max; i++)
            res.push_back(i);
        return res;
    }
};


void test(string test_name, int n, vector<int>& expected)
{
    vector<int> res = Solution().printNumbers(n);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int n1 = 1;
    vector<int> expected1 = {1,2,3,4,5,6,7,8,9};
    test("test1", n1, expected1);

    return 0;
}


// 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。
// 比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

// 示例 1:

// 输入: n = 1
// 输出: [1,2,3,4,5,6,7,8,9]
//  

// 说明：

// 用返回一个整数列表来代替打印
// n 为正整数
