#include <iostream>
#include <stack>
#include "utils_cpp/tree.h"
using namespace std;


class BSTIterator {
    stack<TreeNode*> stk;
public:
    BSTIterator(TreeNode* root) {
        while (root) {
            stk.push(root);
            root = root->left;
        }
    }
    
    /** @return the next smallest number */
    int next() {
        TreeNode *p = stk.top(); stk.pop();
        int res = p->val;
        p = p->right;
        while (p) {
            stk.push(p);
            p = p->left;
        }
        return res;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return !stk.empty();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */

void test1()
{
    //     7
    //    / \
    //   3   15
    //      /  \
    //     9    20
    TreeNode *root = new TreeNode(7);
    root->left = new TreeNode(3);
    root->right = new TreeNode(15);
    root->right->left = new TreeNode(9);
    root->right->right = new TreeNode(20);

    BSTIterator *iter = new BSTIterator(root);
    int res1 = iter->next();      // 3
    int res2 = iter->next();      // 7
    bool res3 = iter->hasNext();  // true
    int res4 = iter->next();      // 9
    bool res5 = iter->hasNext();  // true
    int res6 = iter->next();      // 15
    bool res7 = iter->hasNext();  // true
    int res8 = iter->next();      // 20
    bool res9 = iter->hasNext();  // false
    if (res1 == 3 &&
        res2 == 7 &&
        res3 == true &&
        res4 == 9 &&
        res5 == true &&
        res6 == 15 &&
        res7 == true &&
        res8 == 20 &&
        res9 == false
    )
        cout << "test1 success." << endl;
    else
        cout << "test1 failed." << endl;
}

int main()
{
    test1();
    return 0;
}

// Implement an iterator over a binary search tree (BST). 
// Your iterator will be initialized with the root node of a BST.

// Calling next() will return the next smallest number in the BST.

// Example:

// BSTIterator iterator = new BSTIterator(root);
// iterator.next();    // return 3
// iterator.next();    // return 7
// iterator.hasNext(); // return true
// iterator.next();    // return 9
// iterator.hasNext(); // return true
// iterator.next();    // return 15
// iterator.hasNext(); // return true
// iterator.next();    // return 20
// iterator.hasNext(); // return false
//  

// Note:

// next() and hasNext() should run in average O(1) time and uses O(h) memory,
// where h is the height of the tree.
// You may assume that next() call will always be valid, that is,
// there will be at least a next smallest number in the BST when next() is called.
