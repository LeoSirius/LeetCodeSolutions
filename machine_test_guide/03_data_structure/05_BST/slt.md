### 思路1 先构建BST，然后遍历输出

```cpp
#include<iostream>
#include<string>
using namespace std;

struct Node{
    Node *left;
    Node *right;
    int value;
};

Node *create(){
    Node *node = new Node();
    node->left = node->right = nullptr;
    return node;
}

Node *insert(Node *T, int x){
    if(T == nullptr){
        T = create();
        T->value = x;
        return T;
    }else if(x < T->value){
        T->left = insert(T->left, x);
    }else{
        T->right = insert(T->right, x);
    }
    return T;
}

void pre_order(Node *T){
    if(T == nullptr){
        return;
    }
    printf("%d ", T->value);
    pre_order(T->left);
    pre_order(T->right);
}

void in_order(Node *T){
    if(T == nullptr){
        return;
    }
    in_order(T->left);
    printf("%d ", T->value);
    in_order(T->right);
}

void post_order(Node *T){
    if(T == nullptr){
        return;
    }
    post_order(T->left);
    post_order(T->right);
    printf("%d ", T->value);
}

int main(){
    int n;
    while(scanf("%d", &n) != EOF){
        Node *T = nullptr;
        for(int i = 0; i < n; ++i){
            int x;
            scanf("%d", &x);
            T = insert(T, x);
        }
        pre_order(T); cout << endl;
        in_order(T); cout << endl;
        post_order(T); cout << endl;
    }
    return 0;
}
```