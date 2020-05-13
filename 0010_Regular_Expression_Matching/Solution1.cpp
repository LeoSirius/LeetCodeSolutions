#include <iostream>
using namespace std;

class Solution {
    bool is_match(const char *s, const char *p)
    {
        if (*p == 0) return *s == 0;      //  必须是p先为空，再检查s。意思是模式串完了，输入串刚好匹配完
        bool first_match = *s && (*s == *p || *p == '.');
        if (*(p+1) == '*') {
            // 第一种情况是s中没有p中*的preceding char。即把p中*前面的字符跳过
            // s=abc, p=d*abc
            // 第二种情况是s中有p中*的preceding char，*匹配了preceding char
            // s=aaac, p=a*c
            return is_match(s, p+2) || (first_match && is_match(++s, p));
        } else {
            return first_match && is_match(++s, ++p);
        }
    }
public:
    bool isMatch(string s, string p) {
        return is_match(s.c_str(), p.c_str());
    }
};

void test(string test_name, string s, string p, bool expected)
{
    bool res = Solution().isMatch(s, p);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "aa";
    string p1 = "a";
    bool expected1 = false;
    test("test1", s1, p1, expected1);

    string s2 = "aa";
    string p2 = "a*";
    bool expected2 = true;
    test("test2", s2, p2, expected2);

    string s3 = "ab";
    string p3 = ".*";  // ".*" means "zero or more (*) of any character (.)".
    bool expected3 = true;
    test("test3", s3, p3, expected3);

    string s4 = "aab";
    string p4 = "c*a*b";
    bool expected4 = true;
    test("test4", s4, p4, expected4);

    string s5 = "mississippi";
    string p5 = "mis*is*p*.";
    bool expected5 = false;
    test("test5", s5, p5, expected5);

    return 0;
}
