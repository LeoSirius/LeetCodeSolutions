#include <iostream>
using namespace std;

class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s == t)
            return true;
        if (s == "")
            return true;
        int ps = 0, pt = 0;
        while (ps < s.size() && pt < t.size()) {
            if (s[ps] == t[pt]) {
                ps++; pt++;
            } else {
                pt++;
            }
        }
        return ps == s.size();
    }
};

void test(string test_name, string s, string t, bool expected)
{
    bool res = Solution().isSubsequence(s, t);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    string s1 = "abc";
    string t1 = "ahbgdc";
    bool expected1 = true;
    test("test1", s1, t1, expected1);

    string s2 = "axc";
    string t2 = "ahbgdc";
    bool expected2 = false;
    test("test2", s2, t2, expected2);

    return 0;
}

// Given a string s and a string t, check if s is subsequence of t.

// A subsequence of a string is a new string which is formed from 
// the original string by deleting some (can be none) of the characters 
// without disturbing the relative positions of the remaining characters.
//  (ie, "ace" is a subsequence of "abcde" while "aec" is not).

// Follow up:
// If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, 
// and you want to check one by one to see if T has its subsequence. 
// In this scenario, how would you change your code? 

// Example 1:
// Input: s = "abc", t = "ahbgdc"
// Output: true

// Example 2:
// Input: s = "axc", t = "ahbgdc"
// Output: false
//  

// Constraints:

// 0 <= s.length <= 100
// 0 <= t.length <= 10^4
// Both strings consists only of lowercase characters.
