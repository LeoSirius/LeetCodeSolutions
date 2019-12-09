#include<iostream>
#include<vector>
using namespace std;
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    vector<int> my_preorder;
    vector<int> my_inorder;
    TreeNode *build_tree(int pb, int pe, int ib, int ie)
    {
        // TreeNode *node;
        TreeNode *node = new TreeNode(my_preorder[pb]);
        int root_idx_in_in = ib;
        for (int i = ib; i <= ie; i++) {
            if (my_inorder[i] == node->val) {
                root_idx_in_in = i;
                break;
            }
        }

        int left_node_num = root_idx_in_in - ib;
        if (root_idx_in_in > ib) {
            node->left = build_tree(pb + 1, pb + left_node_num, ib, root_idx_in_in - 1);
        }
        if (root_idx_in_in < ie) {
            node->right = build_tree(pb + left_node_num + 1, pe, root_idx_in_in + 1, ie);
        }
        return node;
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        if (preorder.size() != inorder.size() || preorder.size() == 0 || inorder.size() == 0)
            return nullptr;
        my_preorder = preorder;
        my_inorder = inorder;
        return build_tree(0, my_preorder.size() - 1, 0, my_inorder.size() - 1);
    }
};

void get_postorder(TreeNode *T, vector<int> &postorder)
{
    if (T == nullptr)
        return;
    get_postorder(T->left, postorder);
    get_postorder(T->right, postorder);
    postorder.push_back(T->val);
}

void test(string test_name, vector<int> &preorder, vector<int> &inorder, vector<int> &expected_post)
{
    Solution s;
    vector<int> postorder;
    TreeNode *tree = s.buildTree(preorder, inorder);
    
    get_postorder(tree, postorder);
    if (postorder == expected_post) {
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
    vector<int> expected1 = {9, 15, 7, 20, 3};
    test("test1", pre1, in1, expected1);

    vector<int> pre2 = {};
    vector<int> in2 = {};
    vector<int> expected2 = {};
    test("test2", pre2, in2, expected2);

    return 0;
}
