#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (string str : strs) {
            string tmp = str;
            sort(tmp.begin(), tmp.end());
            // 这里不用find来判断key是否存在，如果不存在，会默认初始化为空vector
            mp[tmp].push_back(str);
        }
        vector<vector<string>> res;
        for (auto pair : mp) {
            res.push_back(pair.second);
        }
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
