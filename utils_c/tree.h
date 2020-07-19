
#ifndef TREE_H
#define TREE_H

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode *new_tree_node(int);

#endif