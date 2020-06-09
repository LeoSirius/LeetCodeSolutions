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

        TreeNode *p;
        queue<TreeNode*> que;
        que.push(root);
        int cur_level = 0;

        while (!que.empty()) {
            int cur_border_size = que.size();
            vector<int> row;
            while (cur_border_size--) {
                p = que.front(); que.pop();
                row.push_back(p->val);
                if (p->left) que.push(p->left);
                if (p->right) que.push(p->right);
            }
            cur_level++;
            if (cur_level % 2 == 0) {
                reverse(row.begin(), row.end());
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
        {20,9},
        {15,7}
    };
    test("test1", root1, expected1);

    return 0;
}

// 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，
// 第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

// 例如:
// 给定二叉树: [3,9,20,null,null,15,7],

//     3
//    / \
//   9  20
//     /  \
//    15   7
// 返回其层次遍历结果：

// [
//   [3],
//   [20,9],
//   [15,7]
// ]
//  

// 提示：
// 节点总数 <= 1000
