#include <iostream>
#include <vector>
#include "util_cpp/tree.h"
using namespace std;

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> res;
    void dfs(TreeNode* root) {
        if (root == nullptr) return;
        if (root->left) inorderTraversal(root->left);
        res.push_back(root->val);
        if (root->right) inorderTraversal(root->right);
    }
    vector<int> inorderTraversal(TreeNode* root) {
        dfs(root);
        return res;
    }
};


void test(string test_name, TreeNode *tree, vector<int> expected)
{
    vector<int> res = Solution().inorderTraversal(tree);
    if (res == expected) {
        cout << test_name << " succeed" << endl;
    } else {
        cout << test_name << " fail" << endl;
    }
}

int main()
{
    TreeNode *root1 = new TreeNode(1);
    root1->right = new TreeNode(2);
    root1->right->left = new TreeNode(3);
    vector<int> expected1 = {1,3,2};
    test("test1", root1, expected1);

    return 0;
}
