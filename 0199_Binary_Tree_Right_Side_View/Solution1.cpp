#include <iostream>
#include <vector>
#include <queue>
#include "utils_cpp/tree.h"
using namespace std;


class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        if (!root) return res;

        TreeNode *p;
        queue<TreeNode*> que;
        que.push(root);
        while (!que.empty()) {
            int cur_border_size = que.size();
            while (cur_border_size--) {
                p = que.front(); que.pop();

                if (cur_border_size == 0)
                    res.push_back(p->val);

                if (p->left) que.push(p->left);
                if (p->right) que.push(p->right);
            }
        }
        return res;
    }
};

void test(string test_name, TreeNode* root, vector<int> expected)
{
    vector<int> res = Solution().rightSideView(root);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    TreeNode *root1 = new TreeNode(1);
    root1->left = new TreeNode(2);
    root1->left->right = new TreeNode(5);
    root1->right = new TreeNode(3);
    root1->right->right = new TreeNode(4);
    vector<int> expected1 = {1,3,4};
    //    1            <---
    //  /   \
    // 2     3         <---
    //  \     \
    //   5     4       <---
    test("test1", root1, expected1);

    return 0;
}


// Given a binary tree, imagine yourself standing on the right side of it, 
// return the values of the nodes you can see ordered from top to bottom.

