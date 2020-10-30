#ifndef TREE_H
#define TREE_H

#include <iostream>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool is_equal_tree(TreeNode* t1, TreeNode* t2);

#endif