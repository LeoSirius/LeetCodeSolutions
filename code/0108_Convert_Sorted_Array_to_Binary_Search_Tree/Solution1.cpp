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
    vector<int> my_nums;
    TreeNode* build_tree(int l, int r)
    {
        int mid = l + (r - l) / 2;
        TreeNode *node = new TreeNode(my_nums[mid]);
        if (mid - l > 0) {
            node->left = build_tree(l, mid - 1);
        }
        if (r - mid > 0) {
            node->right = build_tree(mid + 1, r);
        }
        return node;
    }
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if (nums.empty()) return nullptr;
        my_nums = nums;
        return build_tree(0, nums.size() - 1);
    }
};

void get_inorder(TreeNode *node, vector<int>& inorder)
{
    if (node->left)
        get_inorder(node->left, inorder);
    inorder.push_back(node->val);
    if (node->right)
        get_inorder(node->right, inorder);
}

void test(string test_name, vector<int>& nums, TreeNode *node)
{
    // 测试思路：构建后的BST的中序遍历必然和nums是一样的
    vector<int> pre_res, in_res, pre_exp, in_exp;
    TreeNode *res_node = Solution().sortedArrayToBST(nums);
    if (res_node == node && res_node == nullptr) {
        cout << test_name << " success." << endl;
        return;
    }
    get_inorder(res_node, in_res);
    if (nums == in_res) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed."<< endl;
    }
}

int main()
{
    vector<int> nums1 = {-10, -3, 0, 5, 9};
    TreeNode* root1 = new TreeNode(0);
    root1->left = new TreeNode(-3);
    root1->left->left = new TreeNode(-10);
    root1->right = new TreeNode(9);
    root1->right->left = new TreeNode(5);
    test("test1", nums1, root1);

    vector<int> nums2 = {};
    TreeNode* root2 = nullptr;
    test("test2", nums2, root2);

    return 0;
}
