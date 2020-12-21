#include "utils_cpp/tree.h"
#include <iostream>
using namespace std;

class Solution {
    bool is_mirror(TreeNode* l, TreeNode* r)
    {
        if (!l && !r)
            return true;
        if (!l || !r)
            return false;
        if (l->val != r->val)
            return false;
        return is_mirror(l->left, r->right) && is_mirror(l->right, r->left);
    }
public:
    bool isSymmetric(TreeNode* root) {
        if (!root)
            return true;
        return is_mirror(root->left, root->right);
    }
};


void test(string test_name, TreeNode *root, bool expected)
{
    Solution s;
    if (s.isSymmetric(root) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    TreeNode *t1 = new TreeNode(1);
    t1->left = new TreeNode(2);
    t1->right = new TreeNode(2);
    t1->left->left = new TreeNode(3);
    t1->left->right = new TreeNode(4);
    t1->right->left = new TreeNode(4);
    t1->right->right = new TreeNode(3);
    bool expected1 = true;
    //     1
    //    / \
    //   2   2
    //  / \ / \
    // 3  4 4  3
    test("test1", t1, expected1);

    TreeNode *t2 = new TreeNode(1);
    t2->left = new TreeNode(2);
    t2->left->right = new TreeNode(3);
    t2->right = new TreeNode(2);
    t2->right->right = new TreeNode(3);
    bool expected2 = false;
    //     1
    //    / \
    //   2   2
    //    \   \
    //    3    3
    test("test2", t2, expected2);

    TreeNode *t3 = nullptr;
    bool expected3 = true;
    test("test3", t3, expected3);

    return 0;
}
