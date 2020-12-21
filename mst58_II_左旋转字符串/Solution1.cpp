#include <iostream>
using namespace std;

class Solution {
public:
    string reverseLeftWords(string s, int n) {
        return s.substr(n) + s.substr(0, n);
    }
};

void test(string test_name, string s, int n, string expeceted)
{
    string res = Solution().reverseLeftWords(s, n);
    if (res == expeceted)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    string s1 = "abcdefg";
    int n1 = 2;
    string expected1 = "cdefgab";
    test("test1", s1, n1, expected1);

    string s2 = "lrloseumgh";
    int n2 = 6;
    string expected2 = "umghlrlose";
    test("test2", s2, n2, expected2);

    return 0;
}

// 字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
// 请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，
// 该函数将返回左旋转两位得到的结果"cdefgab"。

// 示例 1：
// 输入: s = "abcdefg", k = 2
// 输出: "cdefgab"

// 示例 2：
// 输入: s = "lrloseumgh", k = 6
// 输出: "umghlrlose"
//  

// 限制：
// 1 <= k < s.length <= 10000
