#include <iostream>
using namespace std;


class Node {
public:
    int val;
    Node* left;
    Node* right;

    Node() {}

    Node(int _val) {
        val = _val;
        left = NULL;
        right = NULL;
    }

    Node(int _val, Node* _left, Node* _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};

class Solution {
    Node *head, *pre;
    void dfs(Node *node)
    {
        if (!node) return;

        dfs(node->left);
        // first node
        if (!head) {
            head = node;
            pre = node;
        } else {
            pre->right = node;
            node->left = pre;
            pre = node;
        }
        dfs(node->right);
    }
public:
    Node* treeToDoublyList(Node* root) {
        if (!root)
            return nullptr;
        head = nullptr;
        dfs(root);
        head->left = pre;
        pre->right = head;
        return head;
    }
};

bool is_equal(Node* head1, Node* head2)
{
    Node *p1 = head1, *p2 = head2;
    if (p1->val != p2->val)
        return false;
    p1 = p1->right; p2 = p2->right;
    while (p1 != head1 && p2 != head2) {
        if (p1->val != p2->val)
            return false;
        p1 = p1->right; p2 = p2->right;
    }
    return true;
}

void test(string test_name, Node* root, Node* expected)
{
    Node *res = Solution().treeToDoublyList(root);
    if (is_equal(res, expected))
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}


int main()
{
    //     4
    //    / \
    //   2   5
    //  / \
    // 1   3
    Node *root1 = new Node(4);
    root1->left = new Node(2);
    root1->left->left = new Node(1);
    root1->left->right = new Node(3);
    root1->right = new Node(5);
    // 1 -> 2 -> 3 -> 4 -> 5
    Node *expected1 = new Node(1);
    expected1->right = new Node(2);
    expected1->right->right = new Node(3);
    expected1->right->right->right = new Node(4);
    expected1->right->right->right->right = new Node(5);
    expected1->right->right->right->right->right = expected1;
    expected1->left = expected1->right->right->right->right->right;
    expected1->right->left = expected1;
    expected1->right->right->left = expected1->right;
    expected1->right->right->right->left = expected1->right->right;
    expected1->right->right->right->right->left = expected1->right->right->right;
    expected1->right->right->right->right->right->left = expected1->right->right->right->right;

    test("test1", root1, expected1);

    return 0;
}
