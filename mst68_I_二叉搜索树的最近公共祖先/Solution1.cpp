#include <iostream>
#include "utils_cpp/tree.h"
using namespace std;


class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root)
            return nullptr;
        
        if (root->val < p->val && root->val < q->val)
            return lowestCommonAncestor(root->right, p, q);
        else if (p->val < root->val && q->val < root->val)
            return lowestCommonAncestor(root->left, p, q);
        // root == p || root == q
        return root;
    }
};

void test(string test_name, TreeNode* root, TreeNode* p, TreeNode* q, TreeNode* expected)
{
    TreeNode* res = Solution().lowestCommonAncestor(root, p, q);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    //      6
    //    /   \
    //   2     8
    //  / \   / \
    // 0   4 7   9
    //    / \
    //   3   5
    TreeNode* root1 = new TreeNode(6);
    root1->left = new TreeNode(2);
    root1->left->left = new TreeNode(0);
    root1->left->right = new TreeNode(4);
    root1->left->right->left = new TreeNode(3);
    root1->left->right->right = new TreeNode(0);

    root1->right = new TreeNode(8);
    root1->right->left = new TreeNode(7);
    root1->right->right = new TreeNode(9);

    TreeNode* p1 = root1->left;
    TreeNode* q1 = root1;

    TreeNode* expected1 = root1;
    // p1 = 6, q1 = 2, expected1 = 6
    test("test1", root1, p1, q1, expected1);

    return 0;
}
