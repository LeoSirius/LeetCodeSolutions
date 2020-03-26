#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        int start = 0, min_len = INT32_MAX;
        int left = 0, right = 0;
        int match = 0;

        unordered_map<char, int> window, targets;

        for (auto ch : t)
            targets[ch]++;

        while (right < s.size()) {
            char ch_right = s[right];
            if (targets.count(ch_right)) {
                window[ch_right]++;
                if (window[ch_right] == targets[ch_right])
                    ++match;
            }
            ++right;

            while (match == targets.size()) {
                int new_len = right - left;
                if (new_len < min_len) {
                    start = left;
                    min_len = new_len;
                }

                char ch_left = s[left];
                if (targets.count(ch_left)) {
                    window[ch_left]--;
                    if (window[ch_left] < targets[ch_left])
                        --match;
                }
                ++left;
            }
        }

        return min_len == INT32_MAX ? "" : s.substr(start, min_len);
    }
};

void test(string test_name, string s, string t, string expected)
{
    string res = Solution().minWindow(s, t);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string s1 = "ADOBECODEBANC";
    string t1 = "ABC";
    string expected1 = "BANC";
    test("test1", s1, t1, expected1);

    return 0;
}