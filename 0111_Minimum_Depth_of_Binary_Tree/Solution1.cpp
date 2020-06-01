#include <iostream>
#include "utils_cpp/tree.h"
using namespace std;

class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root)
            return 0;
        int left = minDepth(root->left);
        int right = minDepth(root->right);
        return (left && right) ? min(left, right) + 1 : left + right + 1;
    }
};

void test(string test_name, TreeNode *root, int expected)
{
    int res = Solution().minDepth(root);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7
    // return its minimum depth = 2.
    TreeNode *root1 = new TreeNode(3);
    root1->left = new TreeNode(9);
    root1->right = new TreeNode(20);
    root1->right->left = new TreeNode(15);
    root1->right->right = new TreeNode(7);
    int expected1 = 2;
    test("test1", root1, expected1);

    //   1
    //  /
    // 2
    TreeNode *root2 = new TreeNode(1);
    root2->left = new TreeNode(2);
    int expected2 = 2;
    test("test2", root2, expected2);

    return 0;
}
