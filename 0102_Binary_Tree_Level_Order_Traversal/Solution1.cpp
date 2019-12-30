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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res;
        if (!root) return res;

        queue<TreeNode*> my_queue;
        my_queue.push(root);
        while (!my_queue.empty()) {
            int count = my_queue.size();
            vector<int> row;
            while (count) {
                TreeNode *cur_node = my_queue.front(); my_queue.pop();
                row.push_back(cur_node->val);
                count--;
                if (cur_node->left) {
                    my_queue.push(cur_node->left);
                }
                if (cur_node->right) {
                    my_queue.push(cur_node->right);
                }
            }
            res.push_back(row);
        }
        return res;
    }
};

void test(string test_name, TreeNode *root, vector<vector<int>> expected)
{
    Solution s;
    if (s.levelOrder(root) == expected) {
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
        {3}, {9, 20}, {15, 7}
    };
    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7
    test("test1", t1, expected1);

    TreeNode *t2 = nullptr;
    vector<vector<int>> expected2;
    test("test2", t2, expected2);

    return 0;
}
