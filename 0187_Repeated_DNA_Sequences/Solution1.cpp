#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> res;
        if (s.size() <= 10) return res;
        unordered_map<string, int> mp;
        // 如果有11个。11 - 10 = 1，i可以取到1
        for (int i = 0; i <= s.size() - 10; i++) {
            ++mp[s.substr(i, 10)];
        }
        for (auto pair : mp) {
            if (pair.second > 1) {
                res.push_back(pair.first);
            }
        }
        return res;
    }
};

void test(string test_name, string s, vector<string> expected)
{
    vector<string> res = Solution().findRepeatedDnaSequences(s);
    sort(res.begin(), res.end());
    sort(expected.begin(), expected.end());
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}


int main()
{
    string s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
    vector<string> expected1 = {"AAAAACCCCC", "CCCCCAAAAA"};
    test("test1", s1, expected1);

    string s2 = "AAAAAAAAAAA";
    vector<string> expected2 = {"AAAAAAAAAA"};
    test("test2", s2, expected2);

    return 0;
}
