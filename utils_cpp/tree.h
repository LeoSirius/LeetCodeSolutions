#include <iostream>
using namespace std;

#ifndef TREE_H
#define TREE_H

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

bool is_same_tree(TreeNode* t1, TreeNode* t2);

#endif