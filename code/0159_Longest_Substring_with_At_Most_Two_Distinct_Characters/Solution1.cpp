#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        int res = 0, left = 0;
        unordered_map<char, int> m;
        for (int i = 0; i < s.size(); ++i) {
            ++m[s[i]];
            while (m.size() > 2) {
                if (--m[s[left]] == 0) m.erase(s[left]);
                ++left;
            }
            res = max(res, i - left + 1);
        }
        return res;
    }
};

void test(string test_name, string s, int expected)
{
    if (Solution().lengthOfLongestSubstringTwoDistinct(s) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "eceba";
    int expected1 = 3;    // "ece" which its length is 3.
    test("test1", s1, expected1);

    string s2 = "ccaabbb";
    int expected2 = 5;    // "aabbb" which its length is 5.
    test("test2", s2, expected2);

    return 0;
}
