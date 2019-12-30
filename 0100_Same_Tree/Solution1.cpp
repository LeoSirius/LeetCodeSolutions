#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    bool is_same(TreeNode *p, TreeNode *q)
    {
        if (p == nullptr && q == nullptr) return true;
        if (p == nullptr || q == nullptr) return false;
        if (p->val == q->val)
            if (is_same(p->left, q->left) && is_same(p->right, q->right))
                return true;
        return false;
    }
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return is_same(p, q);
    }
};

void test(string test_name, TreeNode* p, TreeNode* q, bool expected)
{
    Solution s;
    if (s.isSameTree(p, q) == expected) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    TreeNode* p1 = new TreeNode(1);
    p1->left = new TreeNode(2);
    p1->right = new TreeNode(3);
    TreeNode* q1 = new TreeNode(1);
    q1->left = new TreeNode(2);
    q1->right = new TreeNode(3);
    bool expected1 = true;
    // Input:     1         1
    //           / \       / \
    //          2   3     2   3
    // Output: true
    test("test1", p1, q1, expected1);


    TreeNode *p2 = new TreeNode(1);
    p2->left = new TreeNode(2);
    TreeNode *q2 = new TreeNode(1);
    q2->right = new TreeNode(2);
    bool expected2 = false;
    // Input:     1         1
    //           /           \
    //          2             2
    // Output: false
    test("test2", p2, q2, expected2);

    TreeNode *p3 = new TreeNode(1);
    p3->left = new TreeNode(2);
    p3->right = new TreeNode(1);
    TreeNode *q3 = new TreeNode(1);
    q3->left = new TreeNode(1);
    q3->right = new TreeNode(2);
    bool expected3 = false;
    // Input:     1         1
    //           / \       / \
    //          2   1     1   2
    // Output: false
    test("test3", p3, q3, expected3);

    return 0;
}
