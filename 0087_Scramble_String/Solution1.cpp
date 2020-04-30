#include <iostream>
using namespace std;

class Solution {
public:
    bool isScramble(string s1, string s2) {
        if (s1 == s2)
            return true;
        char ch_cnt[26] = {0};
        for (int i = 0; s1[i]; ++i) {
            ch_cnt[s1[i] - 'a']++;
            ch_cnt[s2[i] - 'a']--;
        }
        for (int i = 0; i < 26; ++i)
            if (ch_cnt[i] != 0)
                return false;

        int len = s1.size();
        for (int i = 1; i < len; ++i) {
            // substr是左闭右开的
            if (isScramble(s1.substr(0, i), s2.substr(0, i)) && isScramble(s1.substr(i), s2.substr(i)))
                return true;
            if (isScramble(s1.substr(0, i), s2.substr(len-i)) && isScramble(s1.substr(i), s2.substr(0,len-i)))
                return true;
        }
        return false;
    }
};


void test(string test_name, string s1, string s2, bool expected)
{
    bool res = Solution().isScramble(s1, s2);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s11 = "great", s21 = "rgeat";
    bool expected1 = true;
    test("test1", s11, s21, expected1);

    string s12 = "abcde", s22 = "caebd";
    bool expected2 = false;
    test("test2", s12, s22, expected2);

    string s13 = "abc", s23 = "bca";
    bool expected3 = true;
    test("test3", s13, s23, expected3);

    return 0;
}
