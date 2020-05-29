#include <iostream>
#include <vector>
#include "utils_cpp/tree.h"
using namespace std;

class Solution {
    vector<int> preorder;
    vector<int> inorder;

    TreeNode* build(int s1, int e1, int s2, int e2)
    {
        int root_val = this->preorder[s1];
        int root_idx = s2;
        for (int i = s2; i <= e2; i++)
            if (this->inorder[i] == root_val) {
                root_idx =i;
                break;
            }

        TreeNode *new_node = new TreeNode(root_val);
        
        int left_cnt = root_idx - s2;
        int right_cnt = e2 - root_idx;

        if (left_cnt)
            new_node->left = this->build(s1+1, s1+left_cnt, s2, root_idx-1);
        if (right_cnt)
            new_node->right = this->build(s1 + left_cnt + 1, e1, root_idx + 1, e2);

        return new_node;
    }
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        int len = preorder.size();
        if (!len)
            return nullptr;

        this->preorder = preorder;
        this->inorder = inorder;
        return this->build(0, len-1, 0, len-1);
    }
};

void test(string test_name, vector<int>& preorder, vector<int>& inorder, TreeNode* expected)
{
    TreeNode* res = Solution().buildTree(preorder, inorder);
    if (is_equal_tree(res, expected))
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    vector<int> preorder1 = {3,9,20,15,7};
    vector<int> inorder1 = {9,3,15,20,7};
    TreeNode* expected1 = new TreeNode(3);
    expected1->left = new TreeNode(9);
    expected1->right = new TreeNode(20);
    expected1->right->left = new TreeNode(15);
    expected1->right->right = new TreeNode(7);
    test("test1", preorder1, inorder1, expected1);

    return 0;
}