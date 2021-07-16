#include <iostream>
#include <algorithm>
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
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};

void test(string test_name, TreeNode *root, int expected)
{
    int res = Solution().maxDepth(root);
    if (res == expected) {
        cout << test_name << " succeed" << endl;
    } else {
        cout << test_name << " fail" << endl;
    }
}

int main()
{
    TreeNode *t1 = new TreeNode(3);
    t1->left = new TreeNode(9);
    t1->right = new TreeNode(20);
    t1->right->left = new TreeNode(15);
    t1->right->right = new TreeNode(7);
    int expected1 = 3;
    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7
    test("test1", t1, expected1);

    return 0;
}