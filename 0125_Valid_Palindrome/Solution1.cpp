#include <iostream>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        if (s.empty()) return true;
        string pure_str = "";
        for (int i = 0; s[i]; i++) {
            if (isalnum(s[i])) {
                pure_str += tolower(s[i]);
            }
        }
        int l = 0, r = pure_str.size() - 1;
        while (l < r) {
            if (pure_str[l++] != pure_str[r--])
                return false;
        }
        return true;
    }
};

void test(string test_name, string s, bool expected)
{
    bool res = Solution().isPalindrome(s);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "A man, a plan, a canal: Panama";
    bool expected1 = true;
    test("test1", s1, expected1);

    string s2 = "race a car";
    bool expected2 = false;
    test("test2", s2, expected2);

    return 0;
}
