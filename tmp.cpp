#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    vector<int> my_in;
    vector<int> my_post;
    TreeNode* build_tree(int s1, int e1, int s2, int e2)
    {
        int root_idx;
        int root_val = my_post[e2];
        for (int i = s1; i <= e1; i++) {
            if (my_in[i] == root_val) {
                root_idx = i;
                break;
            }
        }

        TreeNode *node = new TreeNode(root_val);
        int item_in_left = root_idx - s1;
        int item_in_right = e1 - root_idx;
        if (item_in_left > 0) {
            node->left = build_tree(s1, root_idx - 1, s2, s2 + item_in_left - 1);
        }
        if (item_in_right > 0) {
            node->right = build_tree(root_idx + 1, e1, s2 + item_in_left, e2 - 1);
        }
        return node;
    }
public:
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        if (inorder.size() == 0) {
            return nullptr;
        }
        my_in = inorder;
        my_post = postorder;
        return build_tree(0, my_in.size()-1, 0, my_post.size()-1);
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