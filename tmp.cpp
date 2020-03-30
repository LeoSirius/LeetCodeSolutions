#include <iostream>
#include <map>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        map<char, int> my_map;
        int max_len = 0, start = 0;
        for (int i = 0; s[i]; i++) {
            if (my_map.count(s[i])) {
                start = max(start, my_map[s[i]] + 1);
            }
            my_map[s[i]] = i;
            max_len = max(max_len, i - start + 1);
        }
        return max_len;
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

    return 0;
}
