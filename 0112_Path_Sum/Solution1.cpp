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
    bool hasPathSum(TreeNode* root, int sum) {
        if (!root) return false;
        if (!root->left && !root->right) {
            return sum - root->val == 0;
        }
        return hasPathSum(root->left, sum - root->val) || hasPathSum(root->right, sum - root->val);
    }
};

void test(string test_name, TreeNode *root, int sum, bool expected)
{
    bool res = Solution().hasPathSum(root, sum);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}


int main()
{
    //       5
    //      / \
    //     4   8
    //    /   / \
    //   11  13  4
    //  /  \      \
    // 7    2      1
    TreeNode* root1 = new TreeNode(5);
    root1->left = new TreeNode(4);
    root1->right = new TreeNode(8);
    root1->left->left = new TreeNode(11);
    root1->left->left->left = new TreeNode(7);
    root1->left->left->right = new TreeNode(2);
    root1->right->left = new TreeNode(13);
    root1->right->right = new TreeNode(4);
    root1->right->right->right = new TreeNode(1);
    int sum1 = 22;
    bool expected1 = true;
    test("test1", root1, sum1, expected1);

    return 0;
}
