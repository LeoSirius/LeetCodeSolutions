#include <iostream>
#include <bitset>
using namespace std;

class Solution {
public:
    int add(int a, int b) {
        int carry;
        // 有进位，则继续循环
        while (b) {
            carry = (unsigned int)(a & b) << 1;
            a ^= b;
            b = carry;
        }
        return a;
    }
};

void test(string test_name, int a, int b, int expected)
{
    int res = Solution().add(a, b);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int a1 = 1, b1 = 1;
    int expected1 = 2;
    test("test1", a1, b1, expected1);

    int a2 = -1, b2 = 2;
    int expected2 = 1;
    test("test2", a2, b2, expected2);

    return 0;
}


// 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。

//  

// 示例:

// 输入: a = 1, b = 1
// 输出: 2
//  

// 提示：

// a, b 均可能是负数或 0
// 结果不会溢出 32 位整数

