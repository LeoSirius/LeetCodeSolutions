#include <iostream>
#include "utils_cpp/tree.h"
using namespace std;

class Solution {
    bool is_sym(TreeNode* l, TreeNode *r)
    {
        if (!l && !r) return true;
        if (!l || !r) return false;
        if (l->val != r->val) return false;
        return is_sym(l->left, r->right) && is_sym(l->right, r->left);
    }
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        return is_sym(root->left, root->right);
    }
};

void test(string test_name, TreeNode* root, bool expected)
{
    bool res = Solution().isSymmetric(root);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    //     1
    //    / \
    //   2   2
    //  / \ / \
    // 3  4 4  3
    TreeNode *root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->left->left = new TreeNode(3);
    root1->left->right = new TreeNode(4);
    root1->right = new TreeNode(2);
    root1->right->left = new TreeNode(4);
    root1->right->right = new TreeNode(3);
    bool expected1 = true;
    test("test1", root1, expected1);

    //     1
    //    / \
    //   2   2
    //    \   \
    //    3    3
    TreeNode *root2 = new TreeNode(1);
    root2->left = new TreeNode(2);
    root2->left->right = new TreeNode(3);
    root2->right = new TreeNode(2);
    root2->right->right = new TreeNode(3);
    bool expected2 = false;
    test("test2", root2, expected2);

    return 0;
}

