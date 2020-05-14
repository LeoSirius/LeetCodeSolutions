#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (string word : strs) {
            string sorted_word = word;
            sort(sorted_word.begin(), sorted_word.end());
            mp[sorted_word].push_back(word);
        }
        vector<vector<string>> res;
        for (auto pair : mp)
            res.push_back(pair.second);
        return res;
    }
};


void test(string test_name, vector<string> &strs, vector<vector<string>> &expected)
{
    vector<vector<string>> res = Solution().groupAnagrams(strs);
    for (int i = 0; i < res.size(); i++) {
        sort(res[i].begin(), res[i].end());
    }
    sort(res.begin(), res.end());
    for (int i = 0; i < expected.size(); i++) {
        sort(expected[i].begin(), expected[i].end());
    }
    sort(expected.begin(), expected.end());
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    vector<string> strs1 = {"eat", "tea", "tan", "ate", "nat", "bat"};
    vector<vector<string>> expected1 = {
        {"ate","eat","tea"},
        {"nat","tan"},
        {"bat"},
    };
    test("test1", strs1, expected1);

    return 0;
}