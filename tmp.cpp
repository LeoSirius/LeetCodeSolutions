#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> mp = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        int res = 0;
        for (int i = 0; i < s.size() - 1; i++) {
            if (mp[s[i]] < mp[s[i+1]])
                res -= mp[s[i]];
            else
                res += mp[s[i]];
        }
        return res + mp[s[s.size()-1]];
    }
};

void test(string test_name, string s, int expected)
{
    Solution solution;
    if (solution.romanToInt(s) == expected) {
        cout << test_name << " success. " << endl;
    } else {
        cout << test_name << " failed. " << endl;
    }
}

int main()
{
    test("test1", "MCMXCIV", 1994);
    return 0;
}
