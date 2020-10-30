#include <iostream>
#include <vector>
#include <stack>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    bool isValidBST(TreeNode* root) {
        vector<int> inorder;
        stack<TreeNode*> stk;
        TreeNode *node = root;
        while (node || !stk.empty()) {
            if (node) {
                stk.push(node);
                node = node->left;
            } else {
                TreeNode *cur_node = stk.top();
                stk.pop();
                inorder.push_back(cur_node->val);
                node = cur_node->right;
            }
        }
        for (int i = 1; i < inorder.size(); i++) {
            if (inorder[i-1] >= inorder[i])
                return false;
        }
        return true;
    }
};

void test(string test_name, TreeNode* root, bool expected)
{
    Solution s;
    if (s.isValidBST(root) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    TreeNode* tree1 = new TreeNode(2);
    tree1->left = new TreeNode(1);
    tree1->right = new TreeNode(3);
    bool expected1 = true;
    //     2
    //    / \
    //   1   3
    // Output: true
    test("test1", tree1, expected1);

    TreeNode* tree2 = new TreeNode(5);
    tree2->left = new TreeNode(1);
    tree2->right = new TreeNode(4);
    tree2->right->left = new TreeNode(3);
    tree2->right->right = new TreeNode(6);
    bool expected2 = false;
    //     5
    //    / \
    //   1   4
    //      / \
    //     3   6
    // Output: false
    test("test2", tree2, expected2);

    TreeNode* tree3 = new TreeNode(10);
    tree3->left = new TreeNode(5);
    tree3->right = new TreeNode(15);
    tree3->right->left = new TreeNode(6);
    tree3->right->right = new TreeNode(20);
    bool expected3 = false;
    //    10
    //   /  \
    //  5   15
    //     /  \
    //    6    20
    //   false
    test("test3", tree3, expected3);

    TreeNode* tree4 = new TreeNode(1);
    tree4->left = new TreeNode(1);
    bool expected4 = false;
    test("test4", tree4, expected4);

    return 0;
}
