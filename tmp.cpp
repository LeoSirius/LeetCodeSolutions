#include<iostream>
using namespace std;

struct node
{
    int value;
    node *left, *right;
};

node *create_node(int value)
{
    node *new_node = new node;
    new_node->value = value;
    new_node->left = new_node->right = nullptr;
    return new_node;
}

node *insert(node *tree, int value)
{
    if (tree == nullptr) {
        tree = create_node(value);
        return tree;
    } else if (value < tree->value) {
        tree->left = insert(tree->left, value);
    } else {
        tree->right = insert(tree->right, value);
    }
    return tree;
}

void pre_order(node *tree)
{
    if (tree == nullptr) return;
    printf("%d ", tree->value);
    pre_order(tree->left);
    pre_order(tree->right);
}

void in_order(node *tree)
{
    if (tree == nullptr) return;
    in_order(tree->left);
    printf("%d ", tree->value);
    in_order(tree->right);
}

void post_order(node *tree)
{
    if (tree == nullptr) return;
    post_order(tree->left);
    post_order(tree->right);
    printf("%d ", tree->value);
}

int main ()
{
    int n;
    while (scanf("%d", &n) != EOF) {
        node *tree = nullptr;
        for (int i = 0; i < n; i++) {
            int value;
            scanf("%d", &value);
            tree = insert(tree, value);
        }
        pre_order(tree);printf("\n");
        in_order(tree);printf("\n");
        post_order(tree);printf("\n");
    }
    return 0;
}