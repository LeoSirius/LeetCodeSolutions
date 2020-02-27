#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    // 这个函数>=0表示层数，-1表示不平衡
    int is_b(TreeNode *root) {
        if (!root)
            return 0;
        int left = is_b(root->left);
        if (left == -1)
            return -1;
        int right = is_b(root->right);
        if (right == -1)
            return -1;
        return abs(left - right) > 1 ? -1 : max(left, right) + 1;
    }
public:
    bool isBalanced(TreeNode* root) {
        return is_b(root) != -1;
    }
};

void test(string test_name, TreeNode *root, bool expected)
{
    bool res = Solution().isBalanced(root);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    TreeNode *root1 = new TreeNode(3);
    root1->left = new TreeNode(9);
    root1->right = new TreeNode(20);
    root1->right->left = new TreeNode(15);
    root1->right->right = new TreeNode(7);
    bool expected1 = true;
    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7
    test("test1", root1, expected1);

    TreeNode* root2 = new TreeNode(1);
    root2->left = new TreeNode(2);
    root2->right = new TreeNode(2);
    root2->left->left = new TreeNode(3);
    root2->left->right = new TreeNode(3);
    root2->left->left->left = new TreeNode(4);
    root2->left->left->right = new TreeNode(4);
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
