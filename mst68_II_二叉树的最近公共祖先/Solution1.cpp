#include <iostream>
#include "./utils_cpp/tree.h"
using namespace std;

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root || p == root || q == root)
            return root;

        // 这个函数返回p或q是第一个参数的子树（包括自身），如果空，则不是子树
        // left,right都不空，说明p和q同时是root->left和root->right的子树
        TreeNode *left = lowestCommonAncestor(root->left, p, q);
        TreeNode *right = lowestCommonAncestor(root->right, p, q);

        // 左右都不是null, pq分别在左右
        if (left && right)
            return root;
        else if (left)    // right == null, pq都在左边
            return left;
        else              // left == null, pq都在右边
            return right;
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
    //      3
    //    /   \
    //   5     1
    //  / \   / \
    // 6   2 0   8
    //    / \
    //   7   4
    TreeNode* root1 = new TreeNode(3);
    root1->left = new TreeNode(5);
    root1->left->left = new TreeNode(6);
    root1->left->right = new TreeNode(2);
    root1->left->right->left = new TreeNode(7);
    root1->left->right->right = new TreeNode(4);

    root1->right = new TreeNode(1);
    root1->right->left = new TreeNode(0);
    root1->right->right = new TreeNode(8);

    TreeNode* p1 = root1->left;
    TreeNode* q1 = root1->right;

    TreeNode* expected1 = root1;
    // p1 = 5, q1 = 1, expected1 = 3
    test("test1", root1, p1, q1, expected1);

    TreeNode* root2 = root1;
    TreeNode* p2 = root2->left;
    TreeNode* q2 = root2->left->right->right;
    TreeNode* expected2 = root2->left;
    // p2 = 5, q2 = 4, expected2 = 5
    test("test2", root2, p2, q2, expected2);

    return 0;
}

// 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

// 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
// 满足 x 是 p、q 的祖先且 x 的深度尽可能大（x本身尽可能的深）（一个节点也可以是它自己的祖先）。”
