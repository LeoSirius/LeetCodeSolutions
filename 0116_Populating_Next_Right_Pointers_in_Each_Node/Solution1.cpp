#include <iostream>
using namespace std;

class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};

class Solution {
public:
    Node* connect(Node* root) {
        if (!root || !root->left) // 叶子节点直接返回。完全二叉树，不用考虑右子树了
            return root;
        // 自己的左右子树连接
        root->left->next = root->right;
        // 自己的右子树和，右边一个的左子树连接
        if (root->next) {
            root->right->next = root->next->left;
        }
        root->left = connect(root->left);
        root->right = connect(root->right);
        return root;
    }
};

// 此题不测