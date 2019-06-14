#include<iostream>
#include<string>
using namespace std;

struct Node{
    Node * left;
    Node * right;
    int v;
}Tree[110];
int loc;

Node * create(){
    Tree[loc].left = Tree[loc].right = nullptr;
    return & Tree[loc++];
}

Node * insert(Node * T, int x){
    if(T == NULL){
        T = create();
        T->v = x;
        return T;
    }else if(x < T->v){
        T->left = insert(T->left, x);
    }else{
        T->right = insert(T->right, x); 
    }
    return T;
}

void post_order(Node *T){
    if(T == NULL){
        return;
    }
    if(T->left){
        post_order(T->left);
    }
    if(T->right){
        post_order(T->right);
    }
    printf("%d ", T->v);
}

void in_order(Node * T){
    if(T == NULL){
        return;
    }
    if(T->left){
        in_order(T->left);
    }
    printf("%d ", T->v);
    if(T->right){
        in_order(T->right);
    } 
}

void pre_order(Node * T){
    if(T == NULL){
        return;
    }
    printf("%d ", T->v);
    if(T->left){
        pre_order(T->left);
    }
    if(T->right){
        pre_order(T->right);
    }
}

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        loc = 0;
        Node *T = nullptr;
        for(int i = 0; i < n; i++){
            int x;
            scanf("%d", &x);
            T = insert(T, x);
        }
        pre_order(T);
        printf("\n");
        in_order(T);
        printf("\n");
        post_order(T);
        printf("\n");
    }
    return 0;
}