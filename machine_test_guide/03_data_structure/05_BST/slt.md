### 思路1 先构建BST，然后遍历输出

```cpp
#include<iostream>
using namespace std;

struct Node {
    Node *left, *right;
    int val;
};

Node *create_node(int x)
{
    Node *node = new Node;
    node->val = x;
    node->left = node->right = nullptr;
    return node;
}

Node *insert(int x, Node *node)
{
    if (node == nullptr) {
        node = create_node(x);
    } else if (x < node->val) {
        node->left = insert(x, node->left);
    } else {
        node->right = insert(x, node->right);
    }
    return node;
}

void preorder(Node *tree)
{
    if (tree == nullptr) return;
    printf("%d ", tree->val);
    preorder(tree->left);
    preorder(tree->right);
}

void inorder(Node *tree)
{
    if (tree == nullptr) return;
    inorder(tree->left);
    printf("%d ", tree->val);
    inorder(tree->right);
}

void postorder(Node *tree)
{
    if (tree == nullptr) return;
    postorder(tree->left);
    postorder(tree->right);
    printf("%d ", tree->val);
}

int main()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        Node *tree_root = nullptr;
        for (int i = 0; i < n; i++) {
            int x;
            scanf("%d", &x);
            tree_root = insert(x, tree_root);
        }
        preorder(tree_root); printf("\n");
        inorder(tree_root); printf("\n");
        postorder(tree_root); printf("\n");
    }
    return 0;
}
```