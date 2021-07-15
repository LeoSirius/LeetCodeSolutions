#include <iostream>
#include "util_cpp/tree.h"
using namespace std;


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p == nullptr && q == nullptr) return true;
        if (p == nullptr || q == nullptr) return false;
        if (p->val != q->val) return false;

        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};


void test(string test_name, TreeNode* p, TreeNode* q, bool expected)
{
    bool res = Solution().isSameTree(p, q);
    if (res == expected) {
        cout << test_name << " succeed" << endl;
    } else {
        cout << test_name << " fail" << endl;
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

    TreeNode *p4 = new TreeNode(0);
    p4->left = new TreeNode(-5);
    TreeNode *q4 = new TreeNode(0);
    q4->left = new TreeNode(-8);
    bool expected4 = false;
    test("test4", p4, q4, expected4);

    return 0;
}
