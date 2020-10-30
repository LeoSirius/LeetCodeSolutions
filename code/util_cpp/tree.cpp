#include "tree.h"

bool is_equal_tree(TreeNode* t1, TreeNode* t2)
{
    if (!t1 && !t2)
        return true;
    if (!t1 || !t2)
        return false;
    if (t1->val != t2->val)
        return false;
    return is_equal_tree(t1->left, t2->left) && is_equal_tree(t1->right, t2->right);
}
