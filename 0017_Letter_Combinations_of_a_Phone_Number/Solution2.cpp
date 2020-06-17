#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
    map<char, string> mp = {{'2',"abc"},{'3',"def"},{'4',"ghi"},{'5',"jkl"},  {'6',"mno"},{'7',"pqrs"},{'8',"tuv"},{'9',"wxyz"}};
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if (digits.empty())  // 如果输入空字符串，需要返回的是[],而不是[""];
            return res;

        string path = "";
        dfs(digits, path, res);
        return res;
    }

    void dfs(string digits, string &path, vector<string> &res)
    {
        if (digits.empty()) {
            res.push_back(path);
            return;
        }
        char ch = digits[0];
        string letters = mp[ch];
        for (char letter : letters) {
            path += letter;
            dfs(digits.substr(1), path, res);
            path.pop_back();
        }
    }
};

void test(string test_name, string digits, vector<string> expected)
{
    // 这道题不管顺序，只要元素一样即可
    vector<string> res = Solution().letterCombinations(digits);
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
    string digits1 = "23";
    vector<string> expected1 = {"ad","ae","af","bd","be","bf","cd","ce","cf"};
    test("test1", digits1, expected1);

    string digits2 = "";
    vector<string> expected2;
    test("test2", digits2, expected2);

    return 0;
}