#include <iostream>
#include <stack>
#include "utils_cpp/tree.h"
using namespace std;

class Solution {
public:
    void recoverTree(TreeNode* root) {
        stack<TreeNode*> stk;
        TreeNode *p = root, *pred = nullptr;  // pred记录之前一个节点，好比较大小
        TreeNode *wronged1 = nullptr, *wronged2 = nullptr;
        while (p != nullptr || !stk.empty()) {
            while (p) {
                stk.push(p);
                p = p->left;
            }
            p = stk.top(); stk.pop();
            
            // 如 1 2 7 4 5 6 3 8
            // 注意第一次进来的时候，pred是需要交换的节点
            // 而第二次进来的时候，p是需要交换的节点
            // 即第一次逆序是第一个，第二次逆序是第二个
            if (pred && p->val < pred->val) {
                wronged2 = p;
                if (wronged1)
                    break;
                wronged1 = pred;
            }
            pred = p;

            p = p->right;
        }
        swap(wronged1->val, wronged2->val);
    }
};

void test(string test_name, TreeNode* root, TreeNode* expected)
{
    Solution().recoverTree(root);
    if (is_same_tree(root, expected))
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    TreeNode *t1 = new TreeNode(1);
    t1->left = new TreeNode(3);
    t1->left->right = new TreeNode(2);

    TreeNode *expected1 = new TreeNode(3);
    expected1->left = new TreeNode(1);
    expected1->left->right = new TreeNode(2);
    test("test1", t1, expected1);

    TreeNode *t2 = new TreeNode(3);
    t2->left = new TreeNode(1);
    t2->right = new TreeNode(4);
    t2->right->left = new TreeNode(2);

    TreeNode *expected2 = new TreeNode(2);
    expected2->left = new TreeNode(1);
    expected2->right = new TreeNode(4);
    expected2->right->left = new TreeNode(3);
    test("test2", t2, expected2);

    return 0;
}