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
    vector<int> pre;
    vector<int> in;
    TreeNode *build_tree(int p1, int p2, int i1, int i2)
    {
        TreeNode *node = new TreeNode(pre[p1]);
        int root_idx = i1;
        for (int i = i1; i <= i2; i++) {
            if (in[i] == node->val) {
                root_idx = i;
                break;
            }
        }
        int left_cnt = root_idx - i1;
        int right_cnt = i2 - root_idx;
        if (root_idx > i1) {
            node->left = build_tree(p1+1, p1+left_cnt, i1, root_idx-1);
        }
        if (root_idx < i2) {
            node->right = build_tree(p1+left_cnt+1, p2, root_idx+1, i2);
        }
        return node;
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        pre = preorder;
        in = inorder;
        if (pre.size() != in.size() || pre.size() == 0) return nullptr;
        return build_tree(0, preorder.size()-1, 0, inorder.size()-1);
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