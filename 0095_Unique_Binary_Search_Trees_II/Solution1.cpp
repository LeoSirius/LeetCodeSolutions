#include <iostream>
#include <vector>
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
    vector<TreeNode*> generateTrees(int start, int end)
    {
        vector<TreeNode*> root_list;
        // 这里加个空指针，保证下面双重循环的时候能够进得去。
        if (start > end) root_list.push_back(nullptr);
        for (int i = start; i <= end; i++) {
            vector<TreeNode*> left_root_list = generateTrees(start, i - 1);
            vector<TreeNode*> right_root_list = generateTrees(i + 1, end);
            for (auto left : left_root_list) {
                for (auto right : right_root_list) {
                    TreeNode *root = new TreeNode(i);
                    root->left = left;
                    root->right = right;
                    root_list.push_back(root);
                }
            }
        }
        return root_list;
    }
public:
    vector<TreeNode*> generateTrees(int n) {
        // if n is 0, expected res is vector<TreeNode*> of size 0
        if (n < 1) return vector<TreeNode*>();
        return generateTrees(1, n);
    }
};

void pre(TreeNode *node, vector<int> &order)
{
    if (node == nullptr) return;
    order.push_back(node->val);
    pre(node->left, order);
    pre(node->right, order);
}

void test(string test_name, int n, vector<vector<int>> expected1)
{
    Solution s;
    vector<TreeNode*> trees = s.generateTrees(n);
    vector<vector<int>> res_orders;
    vector<int> res_order;
    for (auto tree : trees) {
        res_order.clear();
        pre(tree, res_order);
        res_orders.push_back(res_order);
    }

    for (auto item : res_orders) {
        sort(item.begin(), item.end());
    }
    sort(res_orders.begin(), res_orders.end());
    for (auto item : expected1) {
        sort(item.begin(), item.end());
    }
    sort(expected1.begin(), expected1.end());

    if (res_orders == expected1) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    // use preorder to check result tree
    int n1 = 3;
    vector<vector<int>> expected1 = {
        {1,3,2},
        {3,2,1},
        {3,1,2},
        {2,1,3},
        {1,2,3},
    };
    test("test1", n1, expected1);

    int n2 = 0;
    vector<vector<int>> expected2;
    test("test2", n2, expected2);

    return 0;
}
