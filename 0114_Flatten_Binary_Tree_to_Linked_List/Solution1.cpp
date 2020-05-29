#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    TreeNode *last = nullptr;
public:
    void flatten(TreeNode* root) {
        // 按右左根的顺序遍历即可
        if (!root) return;
        if (root->right) flatten(root->right);
        if (root->left) flatten(root->left);
        root->right = last;
        root->left = nullptr;
        last = root;
    }
};

bool is_equal_tree(TreeNode *t1, TreeNode *t2)
{
    if (!t1 && !t2) {
        return true;
    }
    if (!t1 || !t2) {
        return false;
    }
    if (t1->val == t2->val && is_equal_tree(t1->left, t2->left) && is_equal_tree(t1->right, t2->right)) {
        return true;
    }
    return false;
}

void test(string test_name, TreeNode *root, TreeNode *expected)
{
    Solution().flatten(root);
    if (is_equal_tree(root, expected)) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}


int main()
{
    //     1
    //    / \
    //   2   5
    //  / \   \
    // 3   4   6
    // The flattened tree should look like:
    TreeNode *root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->left->left = new TreeNode(3);
    root1->left->right = new TreeNode(4);
    root1->right = new TreeNode(5);
    root1->right->right = new TreeNode(6);

    // 1
    //  \
    //   2
    //    \
    //     3
    //      \
    //       4
    //        \
    //         5
    //          \
    //           6
    TreeNode *expected1 = new TreeNode(1);
    expected1->right = new TreeNode(2);
    expected1->right->right = new TreeNode(3);
    expected1->right->right->right = new TreeNode(4);
    expected1->right->right->right->right = new TreeNode(5);
    expected1->right->right->right->right->right = new TreeNode(6);
    test("test1", root1, expected1);

    return 0;
}
