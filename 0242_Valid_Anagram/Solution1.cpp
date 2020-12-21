#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> m1, m2;
        if (s.size() != t.size()) return false;
        for (int i = 0; s[i]; i++) {
            ++m1[s[i]];
            ++m2[t[i]];
        }
        for (auto pair : m1) {
            if (m2[pair.first] != pair.second) {
                return false;
            }
        }
        return true;
    }
};

void test(string test_name, string s, string t, bool expected)
{
    bool res = Solution().isAnagram(s, t);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "anagram";
    string t1 = "nagaram";
    bool expected1 = true;
    test("test1", s1, t1, expected1);

    string s2 = "rat";
    string t2 = "car";
    bool expected2 = false;
    test("test2", s2, t2, expected2);

    return 0;
}
