#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    int countDigitOne(int n) {
        int res = 0;
        long digit = 1;   // 指向遍历的位数，如i=1即个位，i=10即十位，...，因为n可以有31位，所以10^31用long存储

        // while刚好执行n的位数次
        while (n / digit != 0) {
            long high = n / (10 * digit);        // 如 5014 / (10 * 100) = 5
            long cur = (n / digit) % 10;         // (5014 / 100) % 10 = 0
            long low = n - (n / digit) * digit;  // 5014 - (5014 / 100) * 100 = 14
            if (cur == 0)
                res += high * digit;            // 当前是0，则高位每变化一次，会出现high * digit个1
            else if (cur == 1)
                res += high * digit + low + 1;  // 当前是1，则除了上面的情况，还要加上这一位本身是1的地位的个数
            else
                res += high * digit + digit;    // 高位情况同上，地位如digit=1000，014，1会出现1000次 1000-1999
            digit *= 10;
        }

        return res;
    }
};

void test(string test_name, int n, int expected)
{
    int res = Solution().countDigitOne(n);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int n1 = 12;
    int expected1 = 5;
    test("test1", n1, expected1);

    int n2 = 13;
    int expected2 = 6;
    test("test2", n2, expected2);

    return 0;
}

// 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

// 例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

// 示例 1：
// 输入：n = 12
// 输出：5

// 示例 2：
// 输入：n = 13
// 输出：6
//  

// 限制：
// 1 <= n < 2^31

