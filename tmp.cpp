#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<string> letterCombinations(string digits) {
        string num2ch[10] = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

        vector<string> res;
        
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
