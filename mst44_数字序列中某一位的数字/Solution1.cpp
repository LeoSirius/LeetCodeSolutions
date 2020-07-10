#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    int findNthDigit(int n) {
        // 注意一开始n减1
        n -= 1;
        for (long digits=1;digits < 11;++digits ){
            int first_num = pow(10,digits-1);   // first_num 1, 10, 100, ...
            // 9 * first_num = 9, 90, 900, 
            // 再乘位数，就是当前的宽度
            // 若当前的总宽度大于n，则可以返回结果了

            if (n < 9 * first_num * digits){
                // 比如n=365 一开始减1，354
                // n -= 9 * 1, n = 355
                // n -= 90 * 2, n = 175
                // 175 < 900
                // 100 + 175 / 3 = 158
                // 175 % 3 = 1
                // 即最后的结果5
                return int(to_string(first_num + n/digits)[n%digits])-'0';
            }
            // 把前面的宽度减掉
            n -= 9 * first_num * digits;
        }
        return 0;
    }
};


void test(string test_name, int n, int expected)
{
    int res = Solution().findNthDigit(n);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int n1 = 3;
    int expected1 = 3;
    test("test1", n1, expected1);

    int n2 = 11;
    int expected2 = 0;
    test("test2", n2, expected2);

    int n3 = 365;
    int expected3 = 5;
    test("test3", n3, expected3);

    return 0;
}


// 数字以0123456789101112131415…的格式序列化到一个字符序列中。
// 在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。

// 请写一个函数，求任意第n位对应的数字。

// 示例 1：
// 输入：n = 3
// 输出：3

// 示例 2：
// 输入：n = 11
// 输出：0

// 限制：
// 0 <= n < 2^31
