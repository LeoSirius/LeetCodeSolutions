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
    void dfs(TreeNode *root, int sum, vector<vector<int>> &res, vector<int> path) {
        if (!root) return;
        int remain = sum - root->val;
        path.push_back(root->val);
        if (!root->left && !root->right) {
            if (remain == 0) {
                res.push_back(path);
            }
            return;
        }
        dfs(root->left, remain, res, path);
        dfs(root->right, remain, res, path);
    }
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        vector<int> path;
        dfs(root, sum, res, path);
        return res;
    }
};

void test(string test_name, TreeNode *root, int sum, vector<vector<int>> expected)
{
    vector<vector<int>> res = Solution().pathSum(root, sum);
    sort(res.begin(), res.end());
    sort(expected.begin(), expected.end());
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}


int main()
{
    //       5
    //      / \
    //     4   8
    //    /   / \
    //   11  13  4
    //  /  \    / \
    // 7    2  5   1
    TreeNode* root1 = new TreeNode(5);
    root1->left = new TreeNode(4);
    root1->right = new TreeNode(8);
    root1->left->left = new TreeNode(11);
    root1->left->left->left = new TreeNode(7);
    root1->left->left->right = new TreeNode(2);
    root1->right->left = new TreeNode(13);
    root1->right->right = new TreeNode(4);
    root1->right->right->left = new TreeNode(5);
    root1->right->right->right = new TreeNode(1);
    int sum1 = 22;
    vector<vector<int>> expected1 = {
        {5,4,11,2}, {5,8,4,5}
    };
    test("test1", root1, sum1, expected1);

    return 0;
}
