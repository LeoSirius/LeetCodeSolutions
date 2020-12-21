#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> mp;
        int start = 0;
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
            if (mp.find(s[i]) != mp.end()) {
                start = max(start, mp[s[i]] + 1);
            }
            res = max(res, i - start + 1);
            mp[s[i]] = i;
        }
        return res;
    }
};

void test(string test_name, string s, int expected)
{
    Solution slt;
    if (slt.lengthOfLongestSubstring(s) == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    string s1 = "abcabcbb";
    int expected1 = 3;
    test("test1", s1, expected1);

    string s2 = " ";
    int expected2 = 1;
    test("test2", s2, expected2);

    string s3 = "pwwkew";
    int expected3 = 3;
    test("test3", s3, expected3);

    return 0;
}

// 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。