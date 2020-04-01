#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        int depth = 0;
        vector<int> res;
        for (int i = 0; seq[i]; i++) {
            if (seq[i] == '(') {
                ++depth;
                res.push_back(depth % 2);  // depth分别分配给1和0
            } else {
                res.push_back(depth % 2);  // 右括号和前面一个左括号分的一样
                --depth;
            }
        }
        return res;
    }
};

void test(string test_name, string seq, vector<vector<int>> expected)
{
    vector<int> res = Solution().maxDepthAfterSplit(seq);
    bool pass = false;
    for (auto one_vector : expected) {
        if (res == one_vector)
            pass = true;
    }
    if (pass) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    string seq1 = "(()())";
    vector<vector<int>> expected1 = {
        {0, 1, 1, 1, 1, 0},
        {1,0,0,0,0,1}
    };
    test("test1", seq1, expected1);

    string seq2 = "()(())()";
    vector<vector<int>> expected2 = {
        {0,0,0,1,1,0,1,1},
        {1,1,1,0,0,1,1,1}
    };
    test("test2", seq2, expected2);

    return 0;
}
