#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;
        queue<TreeNode*> que;
        que.push(root);
        TreeNode *p = nullptr;
        while (!que.empty()) {
            int level_cnt = que.size();
            vector<int> level;
            while (level_cnt--) {
                p = que.front();
                que.pop();
                level.push_back(p->val);
                if (p->left)
                    que.push(p->left);
                if (p->right)
                    que.push(p->right);
            }
            res.push_back(level);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};

void test(string test_name, TreeNode* root, vector<vector<int>> expected)
{
    vector<vector<int>> res = Solution().levelOrderBottom(root);
    if (res == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    TreeNode *root1 = new TreeNode(3);
    root1->left = new TreeNode(9);
    root1->right = new TreeNode(20);
    root1->right->left = new TreeNode(15);
    root1->right->right = new TreeNode(7);
    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7
    vector<vector<int>> expected1 = {
        {15, 7}, {9, 20}, {3}
    };
    test("test1", root1, expected1);

    TreeNode *root2 = nullptr;
    vector<vector<int>> expected2 = {};
    test("test2", root2, expected2);

    return 0;
}
