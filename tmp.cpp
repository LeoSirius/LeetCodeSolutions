#include <iostream>
#include <vector>
#include "utils_cpp/tree.h"
using namespace std;

class Solution {
    vector<int> pre;
    vector<int> in;
    TreeNode* build(int s1, int e1, int s2, int e2)
    {
        int root_val = pre[s1];
        int root_idx = s2;
        for (int i = s2; i <= e2; i++) {
            if (in[i] == root_val) {
                root_idx = i;
                break;
            }
        }
        TreeNode *node = new TreeNode(root_val);

        int left_cnt = root_idx - s2;
        int right_cnt = e2 - root_idx;
        if (0 < left_cnt) {
            node->left = build(s1 + 1, s1 + left_cnt, s2, root_idx - 1);
        }
        if (0 < right_cnt) {
            node->right = build(s1 + left_cnt + 1, e1, root_idx + 1, e2);
        }
        return node;
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int len = preorder.size();
        if (!len)
            return nullptr;
        pre = preorder;
        in = inorder;
        return build(0, len - 1, 0, len - 1);
    }
};


void test(string test_name, vector<int> &preorder, vector<int> &inorder, TreeNode *expected)
{
    Solution s;
    vector<int> postorder;
    TreeNode *res = s.buildTree(preorder, inorder);
    
    if (is_same_tree(res, expected)) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    // preorder = [3,9,20,15,7]
    // inorder = [9,3,15,20,7]
    // Return the following binary tree:
    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7
    vector<int> pre1 = {3,9,20,15,7};
    vector<int> in1 = {9,3,15,20,7};
    TreeNode* expected1 = new TreeNode(3);
    expected1->left = new TreeNode(9);
    expected1->right = new TreeNode(20);
    expected1->right->left = new TreeNode(15);
    expected1->right->right = new TreeNode(7);
    test("test1", pre1, in1, expected1);

    vector<int> pre2 = {};
    vector<int> in2 = {};
    TreeNode *expected2 = nullptr;
    test("test2", pre2, in2, expected2);

    return 0;
}