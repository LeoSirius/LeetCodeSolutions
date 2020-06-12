#include <iostream>
#include <vector>
#include <stack>
#include "utils_cpp/tree.h"
using namespace std;

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        if (!root) return res;

        stack<TreeNode*> stk;
        TreeNode *p = root;
        while (!stk.empty() || p != nullptr) {
            while (p) {
                stk.push(p);
                p = p->left;
            }

            p = stk.top(); stk.pop();
            res.push_back(p->val);
            p = p->right;
        }
        return res;
    }
};


void test(string test_name, TreeNode *tree, vector<int> expected)
{
    vector<int> res = Solution().inorderTraversal(tree);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    //    1
    //     \
    //      2
    //     /
    //    3
    TreeNode *root1 = new TreeNode(1);
    root1->right = new TreeNode(2);
    root1->right->left = new TreeNode(3);
    vector<int> expected1 = {1,3,2};
    test("test1", root1, expected1);

    return 0;
}
