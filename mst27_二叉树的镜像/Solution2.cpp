#include <iostream>
#include "utils_cpp/tree.h"
using namespace std;


class Solution {
public:
    TreeNode* mirrorTree(TreeNode* root) {
        if (!root) return nullptr;

        TreeNode *node = root->left;
        root->left = root->right;
        root->right = node;
        mirrorTree(root->left);
        mirrorTree(root->right);
        return root;
    }
};

void test(string test_name, TreeNode* root, TreeNode* expected)
{
    TreeNode *res = Solution().mirrorTree(root);
    if (is_equal_tree(res, expected))
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    //      4
    //    /   \
    //   2     7
    //  / \   / \
    // 1   3 6   9
    TreeNode *root1 = new TreeNode(4);
    root1->left = new TreeNode(2);
    root1->left->left = new TreeNode(1);
    root1->left->right = new TreeNode(3);
    root1->right = new TreeNode(7);
    root1->right->left = new TreeNode(6);
    root1->right->right = new TreeNode(9);

    //      4
    //    /   \
    //   7     2
    //  / \   / \
    // 9   6 3   1
    TreeNode *expected1 = new TreeNode(4);
    expected1->left = new TreeNode(7);
    expected1->left->left = new TreeNode(9);
    expected1->left->right = new TreeNode(6);
    expected1->right = new TreeNode(2);
    expected1->right->left = new TreeNode(3);
    expected1->right->right = new TreeNode(1);

    test("test1", root1, expected1);

    return 0;
}

// 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

// 例如输入：

//      4
//    /   \
//   2     7
//  / \   / \
// 1   3 6   9
// 镜像输出：

//      4
//    /   \
//   7     2
//  / \   / \
// 9   6 3   1

// 限制：
// 0 <= 节点个数 <= 1000