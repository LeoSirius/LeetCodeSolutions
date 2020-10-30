#include "utils_cpp/tree.h"

class Solution {
    int res = INT_MIN;
    // 注意函数返回值，只能是左右子树其中的一个，+当前节点
    // 而res是和，需要左右子树都加起来
    int max_down(TreeNode* node)
    {
        if (!node)
            return 0;
        int left = max(0, max_down(node->left));   // 如果小于0的话，则不走那边
        int right = max(0, max_down(node->right));
        res = max(res, left + right + node->val);
        return max(left, right) + node->val;   // 一个节点往下，只能是左或右
    }
public:
    int maxPathSum(TreeNode* root) {
        max_down(root);
        return res;
    }
};

void test(string test_name, TreeNode* root, int expected)
{
    int res = Solution().maxPathSum(root);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    TreeNode* root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->right = new TreeNode(3);
    int expected1 = 6;
    test("test1", root1, expected1);

    TreeNode* root2 = new TreeNode(-10);
    root2->left = new TreeNode(9);
    root2->right = new TreeNode(20);
    root2->right->left = new TreeNode(15);
    root2->right->right = new TreeNode(7);
    int expected2 = 42;
    test("test2", root2, expected2);

    TreeNode* root3 = new TreeNode(2);
    root3->left = new TreeNode(-1);
    int expected3 = 2;
    test("test3", root3, expected3);

    return 0;
}
