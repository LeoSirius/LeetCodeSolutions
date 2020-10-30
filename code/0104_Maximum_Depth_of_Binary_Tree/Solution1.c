#include <stdio.h>
#include "meta_c/tree.h"

# define MAX(X, Y) ((X) < (Y) ? (Y) : (X))

int maxDepth(struct TreeNode* root){
    if (root == NULL)
        return 0;
    int l_depth = maxDepth(root->left);
    int r_depth = maxDepth(root->right);
    return MAX(l_depth, r_depth) + 1;
}

void test(char test_name[], struct TreeNode *root, int expected)
{
    int res = maxDepth(root);
    if (res == expected)
        printf("%s success.\n", test_name);
    else
        printf("%s failed.\n", test_name);
}

int main()
{
    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7
    struct TreeNode *root1 = new_tree_node(3);
    root1->left = new_tree_node(9);
    root1->right = new_tree_node(20);
    root1->right->left = new_tree_node(15);
    root1->right->right = new_tree_node(7);
    int expected1 = 3;
    test("test1", root1, expected1);

    return 0;
}

