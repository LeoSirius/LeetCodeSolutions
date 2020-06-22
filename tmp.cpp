#include <iostream>
#include <cmath>
using namespace std;

class Solution {
public:
    int countDigitOne(int n) {
        int res = 0;
        long digit = 1;   // 指向遍历的位数，如i=1即个位，i=10即十位，...，因为n可以有31位，所以10^31用long存储

        while (n / digit != 0) {
            
        }
    }
};

// class Solution {
// public:
//     int countDigitOne(int n) {
//        int count = 0;
//        long i = 1;//指向遍历的位数，如i=1即个位，i=10即十位，...，因为n可以有31位，所以10^31用long存储
//        while(n/i!=0){
//            //n/i控制遍历的次数，将所有的位数都遍历完毕
//             long high = n/(10*i);//将当前位之前的所有高位都存在high中
//             long cur = (n/i)%10;//将当前位记录在cur中，即我们每次都需要统计当前位上1出现的次数
//             long low = n-(n/i)*i;
//             if(cur == 0){
//                 count += high * i;
//             } else if(cur == 1){
//                 count += high * i + low + 1;
//             } else {
//                 count += high * i + i;
//             }
//             i = i * 10;//准备遍历下一位
//        }
//        return count;
//     }
// };


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

