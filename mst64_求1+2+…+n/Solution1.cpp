#include <iostream>
using namespace std;

class Solution {
public:
    int sumNums(int n) {
        // 用递归和 && 短路来实现for 和 if
        n && (n += sumNums(n-1));
        return n;
    }
};

void test(string test_name, int n, int expected)
{
    int res = Solution().sumNums(n);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int n1 = 3;
    int expected1 = 6;
    test("test1", n1, expected1);

    int n2 = 9;
    int expected2 = 45;
    test("test2", n2, expected2);

    return 0;
}


// 求 1+2+...+n ，
// 要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

 

// 示例 1：
// 输入: n = 3
// 输出: 6

// 示例 2：
// 输入: n = 9
// 输出: 45
 

// 限制：

// 1 <= n <= 10000
