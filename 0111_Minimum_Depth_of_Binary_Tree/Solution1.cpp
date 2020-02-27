#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root)
            return 0;
        int l = minDepth(root->left);
        int r = minDepth(root->right);
        return (l && r) ? min(l, r) + 1 : l + r + 1;
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

    return 0;
}
