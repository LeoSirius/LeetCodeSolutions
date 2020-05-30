#include <iostream>
#include <vector>
#include <queue>
#include "utils_cpp/tree.h"
using namespace std;


class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root)
            return res;

        queue<TreeNode*> que;
        que.push(root);
        int depth = 0;
        while (!que.empty()) {
            int cur_row_cnt = que.size();
            vector<int> row;
            while (cur_row_cnt--) {
                TreeNode *p = que.front(); que.pop();
                row.push_back(p->val);
                if (p->left)
                    que.push(p->left);
                if (p->right)
                    que.push(p->right);
            }
            depth++;
            if ((depth & 1) == 0)   // 偶数深度，反转
                reverse(row.begin(), row.end());
            res.push_back(row);
        }
        return res;
    }
};


void test(string test_name, TreeNode *root, vector<vector<int>> expected)
{
    Solution s;
    if (s.zigzagLevelOrder(root) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    TreeNode *t1 = new TreeNode(3);
    t1->left = new TreeNode(9);
    t1->right = new TreeNode(20);
    t1->right->left = new TreeNode(15);
    t1->right->right = new TreeNode(7);
    vector<vector<int>> expected1 = {
        {3},
        {20, 9},
        {15, 7}
    };
    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7
    test("test1", t1, expected1);

    return 0;
}
