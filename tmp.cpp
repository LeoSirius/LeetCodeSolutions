#include <iostream>
using namespace std;

class Solution {
    bool match(const char *s, const char *p)
    {
        const char *ss = s;
        const char *star = nullptr;

        while (*s) {
            if (*s == *p || *p == '?') {
                ++s; ++p;
                continue;
            }
            if (*p == '*') {
                star = p++;
                ss = s;
                continue;
            }
            if (star) {
                p = star + 1;
                s = ++ss;
                continue;
            }
            return false;
        }
        while (*p == '*') p++;
        return !*p;
    }
public:
    bool isMatch(string s, string p) {
        return match(s.c_str(), p.c_str());
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
    string p2 = "*";
    bool expected2 = true;
    test("test2", s2, p2, expected2);

    string s3 = "cb";
    string p3 = "?a";
    bool expected3 = false;  // Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
    test("test3", s3, p3, expected3);

    string s4 = "adceb";
    string p4 = "*a*b";
    bool expected4 = true;  // Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
    test("test4", s4, p4, expected4);

    string s5 = "acdcb";
    string p5 = "a*c?b";
    bool expected5 = false;
    test("test5", s5, p5, expected5);

    return 0;
}