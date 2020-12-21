#include <iostream>
#include <vector>
#include <queue>
#include "utils_cpp/tree.h"
using namespace std;

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;

        queue<TreeNode*> que;
        que.push(root);
        TreeNode *p;

        while (!que.empty()) {
            vector<int> row;
            int cur_border_cnt = que.size();
            while (cur_border_cnt--) {
                p = que.front(); que.pop();
                row.push_back(p->val);
                if (p->left) que.push(p->left);
                if (p->right) que.push(p->right);
            }
            res.push_back(row);
        }
        return res;
    }
};

void test(string test_name, TreeNode* root, vector<vector<int>> expected)
{
    vector<vector<int>> res = Solution().levelOrder(root);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{

    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7
    TreeNode *root1 = new TreeNode(3);
    root1->left = new TreeNode(9);
    root1->right = new TreeNode(20);
    root1->right->left = new TreeNode(15);
    root1->right->right = new TreeNode(7);
    vector<vector<int>> expected1 = {
        {3},
        {9,20},
        {15,7}
    };
    test("test1", root1, expected1);

    return 0;
}
