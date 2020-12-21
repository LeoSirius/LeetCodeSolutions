#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if (digits.size() <= 0) return res;
        string num2ch[10] = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

        res.push_back("");
        for (int i = 0; digits[i]; i++) {
            string chars = num2ch[digits[i] - '0'];
            vector<string> tmp;
            for (int j = 0; chars[j]; j++) {
                for (int k = 0; k < res.size(); k++) {
                    tmp.push_back(res[k] + chars[j]);
                }
            }
            res = tmp;
        }
        return res;
    }
};

void test(string test_name, string digits, vector<string> expected)
{
    Solution s;
    // 这道题不管顺序，只要元素一样即可
    vector<string> a = s.letterCombinations(digits);
    vector<string> b = expected;
    sort(a.begin(), a.end());
    sort(expected.begin(), expected.end());
    if (a == b) {
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
}
