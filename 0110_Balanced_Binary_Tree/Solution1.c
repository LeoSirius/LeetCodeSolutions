#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include "meta_c/tree.h"

#define MAX(X, Y) (X > Y ? (X) : (Y))

int depth(struct TreeNode *node)
{
    if (node == NULL)
        return 0;
    int left = depth(node->left);
    if (left == -1) return -1;
    int right = depth(node->right);
    if (right == -1) return -1;
    return abs(left-right) > 1 ? -1 :  MAX(left, right) + 1;
}

bool isBalanced(struct TreeNode* root){
    return depth(root) != -1;
}

void test(const char test_name[], struct TreeNode *root, bool expected)
{
    bool res = isBalanced(root);
    if (res == expected)
        printf("%s success.\n", test_name);
    else
        printf("%s failed.\n", test_name);
}


int main()
{
    struct TreeNode *root1 = new_tree_node(3);
    root1->left = new_tree_node(9);
    root1->right = new_tree_node(20);
    root1->right->left = new_tree_node(15);
    root1->right->right = new_tree_node(7);
    bool expected1 = true;
    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7
    test("test1", root1, expected1);

    struct TreeNode *root2 = new_tree_node(1);
    root2->left = new_tree_node(2);
    root2->right = new_tree_node(2);
    root2->left->left = new_tree_node(3);
    root2->left->right = new_tree_node(3);
    root2->left->left->left = new_tree_node(4);
    root2->left->left->right = new_tree_node(4);
    //        1
    //       / \
    //      2   2
    //     / \
    //    3   3
    //   / \
    //  4   4
    bool expected2 = false;
    test("test2", root2, expected2);

    return 0;
}
