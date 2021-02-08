#include <iostream>
using namespace std;

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int res = 0;
        while (n) {
            res += n & 1;
            n >>= 1;
        }
        return res;
    }
};

void test(string test_name, uint32_t n, int expected)
{
    int res = Solution().hammingWeight(n);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    uint32_t n1 = 0b00000000000000000000000000001011;
    int expected1 = 3;
    test("test1", n1, expected1);

    uint32_t n2 = 0b00000000000000000000000010000000;
    int expected2 = 1;
    test("test2", n2, expected2);

    uint32_t n3 = 0b11111111111111111111111111111101;
    int expected3 = 31;
    test("test3", n3, expected3);

    return 0;
}

// 请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，
// 把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。

// 示例 1：

// 输入：00000000000000000000000000001011
// 输出：3
// 解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。
// 示例 2：

// 输入：00000000000000000000000010000000
// 输出：1
// 解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。
// 示例 3：

// 输入：11111111111111111111111111111101
// 输出：31
// 解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
