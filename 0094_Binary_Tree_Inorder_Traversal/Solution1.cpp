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
    void inorder(TreeNode *node, vector<int> &path)
    {
        if (node == nullptr) return;
        inorder(node->left, path);
        path.push_back(node->val);
        inorder(node->right, path);
    }
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorder(root, res);
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
