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
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        if (root == nullptr) return res;
        stack<TreeNode*> stk;
        TreeNode *cur_node = root;
        while (cur_node != nullptr || !stk.empty()) {
            if (cur_node) {
                stk.push(cur_node);
                cur_node = cur_node->left;
            } else {
                cur_node = stk.top();
                stk.pop();
                res.push_back(cur_node->val);
                cur_node = cur_node->right;
            }
        }
        return res;
    }
};

void test(string test_name, TreeNode *tree, vector<int> expected)
{
    Solution s;
    if (s.inorderTraversal(tree) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    TreeNode *root1 = new TreeNode(1);
    root1->right = new TreeNode(2);
    root1->right->left = new TreeNode(3);
    vector<int> expected1 = {1,3,2};
    test("test1", root1, expected1);

    return 0;
}