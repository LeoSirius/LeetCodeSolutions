#include <iostream>
#include <vector>
#include <deque>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (root == nullptr) return res;
        deque<TreeNode*> my_dq;
        my_dq.push_back(root);
        bool left2right = true;
        while (!my_dq.empty()) {
            int count = my_dq.size();
            vector<int> row;
            while (count--) {
                TreeNode *cur_node = my_dq.front(); my_dq.pop_front();
                row.push_back(cur_node->val);
                if (cur_node->left) {
                    my_dq.push_back(cur_node->left);
                }
                if (cur_node->right) {
                    my_dq.push_back(cur_node->right);
                }
            }
            if (!left2right) {
                reverse(row.begin(), row.end());
            }
            left2right = !left2right;
            res.push_back(row);
        }
        return res;
    }
};

void test(string test_name, TreeNode *root, vector<vector<int>> expected)
{
    Solution s;
    if (s.zigzagLevelOrder(root) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    TreeNode *t1 = new TreeNode(3);
    t1->left = new TreeNode(9);
    t1->right = new TreeNode(20);
    t1->right->left = new TreeNode(15);
    t1->right->right = new TreeNode(7);
    vector<vector<int>> expected1 = {
        {3},
        {20, 9},
        {15, 7}
    };
    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7
    test("test1", t1, expected1);

    return 0;
}
