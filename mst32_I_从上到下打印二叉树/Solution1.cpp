#include <iostream>
#include <vector>
#include <queue>
#include "utils_cpp/tree.h"
using namespace std;

class Solution {
public:
    vector<int> levelOrder(TreeNode* root) {
        vector<int> res;
        if (!root) return res;

        TreeNode *p;
        queue<TreeNode*> que;
        que.push(root);

        while (!que.empty()) {
            int cur_border_cnt = que.size();
            while (cur_border_cnt--) {
                p = que.front(); que.pop();
                res.push_back(p->val);
                if (p->left) que.push(p->left);
                if (p->right) que.push(p->right);
            }
        }
        return res;
    }
};

void test(string test_name, TreeNode* root, vector<int> expected)
{
    vector<int> res = Solution().levelOrder(root);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    //     3
    //    / \
    //   9  20
    //     /  \
    //    15   7
    TreeNode *root1 = new TreeNode(3);
    root1->left = new TreeNode(9);
    root1->right = new TreeNode(20);
    root1->right->left = new TreeNode(15);
    root1->right->right = new TreeNode(7);
    vector<int> expected1 = {3, 9, 20, 15, 7};
    test("test1", root1, expected1);

    return 0;
}


// 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。


// 例如:

//     3
//    / \
//   9  20
//     /  \
//    15   7
// 返回：

// [3,9,20,15,7]
