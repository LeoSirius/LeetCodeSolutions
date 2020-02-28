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
        Node *p_root = root;
        Node *first_before_level = new Node();

        while (root) {
            Node *p = first_before_level;
            while (root) {
                if (root->left) {
                    p->next = root->left;
                    p = p->next;
                }
                if (root->right) {
                    p->next = root->right;
                    p = p->next;
                }
                root = root->next;
            }
            root = first_before_level->next;
            first_before_level->next = nullptr;
        }
        return p_root;
    }
};

// 此题不测
