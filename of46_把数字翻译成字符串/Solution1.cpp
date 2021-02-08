#include <iostream>
using namespace std;

class Solution {
public:
    int translateNum(int num) {
        if (num <= 9)
            return 1;
        // 取最低两位
        int res = num % 100;
        // 按最低两位的大小，可能有两种情况
        if (res <= 9 || 26 <= res)
            return translateNum(num / 10);
        else
            return translateNum(num / 10) + translateNum(num / 100);
    }
};

void test(string test_name, int num, int expected)
{
    int res = Solution().translateNum(num);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    int num1 = 12258;
    int expected1 = 5;
    test("test1", num1, expected1);

    return 0;
}


// 给定一个数字，我们按照如下规则把它翻译为字符串：
// 0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
// 一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

// 示例 1:

// 输入: 12258
// 输出: 5

// 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

// 提示：
// 0 <= num < 2*31

