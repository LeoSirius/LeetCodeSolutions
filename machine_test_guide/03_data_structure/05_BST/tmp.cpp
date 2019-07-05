#include<iostream>
#include<string>
using namespace std;

struct Node{
    Node * left;
    Node * right;
    int v;
};

Node * create_node(){
    Node * tmp_node = new Node();
    tmp_node->left = tmp_node->right = nullptr;
    return tmp_node;
}

Node * insert(Node * T, int v){
    if(T == nullptr){
        T = create_node();
        T->v = v;
        return T;
    }else if(v < T->v){
        T->left = insert(T->left, v);
    }else{
        T->right = insert(T->right, v);
    }
    return T;
}

void preorder(Node * T){
    if(T == nullptr)
        return;
    printf("%d ", T->v);
    preorder(T->left);
    preorder(T->right);
}

void inorder(Node * T){
    if(T == nullptr)
        return;
    inorder(T->left);
    printf("%d ", T->v);
    inorder(T->right);
}

void postorder(Node * T){
    if(T == nullptr)
        return;
    postorder(T->left);
    postorder(T->right);
    printf("%d ", T->v);
}

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        Node * tmp_tree = nullptr;
        int v;
        for(int i = 0; i < n; i++){
            scanf("%d", &v);
            tmp_tree = insert(tmp_tree, v);
        }
        preorder(tmp_tree);
        printf("\n");
        inorder(tmp_tree);
        printf("\n");
        postorder(tmp_tree);
        printf("\n");
    }
    return 0;
}