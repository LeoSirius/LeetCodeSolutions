#include "tree.h"

struct TreeNode *new_tree_node(int val)
{
    struct TreeNode new_node;
    new_node.val = val;
    return &new_node;
}