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
    vector<int> my_in;
    vector<int> my_post;
    TreeNode* build_tree(int i1, int i2, int p1, int p2)
    {
        TreeNode *node = new TreeNode(my_post[p2]);
        int root_in_in = i1;
        for (int i = i1; i <= i2; i++) {
            if (my_in[i] == node->val) {
                root_in_in = i;
                break;
            }
        }
        int left_ele_num = root_in_in - i1;
        if (root_in_in > i1) {
            node->left = build_tree(i1, root_in_in - 1, p1, p1 + left_ele_num - 1);
        }
        if (root_in_in < i2) {
            node->right = build_tree(root_in_in + 1, i2, p1 + left_ele_num, p2 - 1);
        }
        return node;
    }
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (inorder.size() != postorder.size() || inorder.size() == 0)
            return nullptr;
        my_in = inorder;
        my_post = postorder;
        return build_tree(0, inorder.size() - 1, 0, postorder.size() - 1);
    }
};

void get_preorder(TreeNode *T, vector<int> &preorder)
{
    if (T == nullptr)
        return;
    preorder.push_back(T->val);
    get_preorder(T->left, preorder);
    get_preorder(T->right, preorder);
}

void test(string test_name, vector<int> &inorder, vector<int> &postorder, vector<int> &expected_pre)
{
    Solution s;
    vector<int> preorder;
    TreeNode *tree = s.buildTree(inorder, postorder);
    
    get_preorder(tree, preorder);
    if (preorder == expected_pre) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{

    // inorder = [9,3,15,20,7]
    // postorder = [9,15,7,20,3]
    // Return the following binary tree:

    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7

    vector<int> in1 = {9,3,15,20,7};
    vector<int> post1 = {9, 15, 7, 20, 3};
    vector<int> expected1 = {3,9,20,15,7};
    test("test1", in1, post1, expected1);

    vector<int> pre2 = {};
    vector<int> in2 = {};
    vector<int> expected2 = {};
    test("test2", pre2, in2, expected2);

    return 0;
}
