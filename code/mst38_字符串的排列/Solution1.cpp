#include <iostream>
#include <vector>
using namespace std;

class Solution {
    vector<string> res;
public:
    void dfs(string s, int start, int end)
    {
        if (start == end) {
            res.push_back(s);
            return;
        }
        for (int i = start; i <= end; i++) {
            if (start < i && s[i] == s[start]) continue;  // 去掉重复的字符，避免重复的结果
            swap(s[i], s[start]);
            dfs(s, start + 1, end);
        }
    }
    vector<string> permutation(string s) {
        sort(s.begin(), s.end());
        dfs(s, 0, s.size() - 1);
        return res;
    }
};

void test(string test_name, string s, vector<string> expected)
{
    vector<string> res = Solution().permutation(s);
    sort(res.begin(), res.end());
    sort(expected.begin(), expected.end());
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    string s1 = "abc";
    vector<string> expected1 = {"abc","acb","bac","bca","cab","cba"};
    test("test1", s1, expected1);

    return 0;
}

// 输入一个字符串，打印出该字符串中字符的所有排列。

// 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。

// 示例:

// 输入：s = "abc"
// 输出：["abc","acb","bac","bca","cab","cba"]
//  

// 限制：
// 1 <= s 的长度 <= 8
