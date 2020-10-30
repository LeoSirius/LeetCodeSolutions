#include <iostream>
#include <vector>
#include <stack>
#include "utils_cpp/tree.h"
using namespace std;


class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> res;
        if (!root) return res;

        TreeNode *p = nullptr;
        stack<TreeNode*> stk;
        p = root;
        while (!stk.empty() || p) {
            while (p) {
                res.push_back(p->val);
                stk.push(p);
                p = p->left;
            }
            p = stk.top(); stk.pop();
            p = p->right;
        }
        return res;
    }
};

void test(string test_name, TreeNode* root, vector<int> expected)
{
    vector<int> res = Solution().preorderTraversal(root);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
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
    vector<int> expected1 = {1,2,3};
    test("test1", root1, expected1);

    TreeNode *root2 = new TreeNode(1);
    root2->left = new TreeNode(2);
    vector<int> expected2 = {1,2};
    test("test2", root2, expected2);

    return 0;
}
