#include <iostream>
#include <vector>
#include "utils_cpp/tree.h"
using namespace std;

class Solution {
    // 注意path是传值，且没有pop
    void dfs(TreeNode *node, int sum, vector<vector<int>> &res, vector<int> path)
    {
        if (!node) return;
        int remain = sum - node->val;
        path.push_back(node->val);

        // 到底时，刚好==0，则是需要的结果
        if (!node->left && !node->right) {
            if (remain == 0) res.push_back(path);
            return;
        }

        dfs(node->left, remain, res, path);
        dfs(node->right, remain, res, path);
    }
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        if (!root) return res;

        vector<int> path;
        dfs(root, sum, res, path);
        return res;
    }
};


void test(string test_name, TreeNode *root, int sum, vector<vector<int>> expected)
{
    vector<vector<int>> res = Solution().pathSum(root, sum);
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
    //       5
    //      / \
    //     4   8
    //    /   / \
    //   11  13  4
    //  /  \    / \
    // 7    2  5   1
    TreeNode* root1 = new TreeNode(5);
    root1->left = new TreeNode(4);
    root1->right = new TreeNode(8);
    root1->left->left = new TreeNode(11);
    root1->left->left->left = new TreeNode(7);
    root1->left->left->right = new TreeNode(2);
    root1->right->left = new TreeNode(13);
    root1->right->right = new TreeNode(4);
    root1->right->right->left = new TreeNode(5);
    root1->right->right->right = new TreeNode(1);
    int sum1 = 22;
    vector<vector<int>> expected1 = {
        {5,4,11,2}, {5,8,4,5}
    };
    test("test1", root1, sum1, expected1);

    return 0;
}

// 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
// 从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

