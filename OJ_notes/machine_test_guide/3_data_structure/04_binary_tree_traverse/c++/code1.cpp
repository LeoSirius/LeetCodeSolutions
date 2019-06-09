#include<iostream>
#include<string>
using namespace std;

struct Node{
    Node * left;
    Node * right;
    char c;
}Tree[50];
int loc;

Node * craete(){
    Tree[loc].left = Tree[loc].right = NULL;
    return &Tree[loc++];
}

char str1[30], str2[30];

void post_order(Node * T){
    if(T->left){
        post_order(T->left);
    }
    if(T->right){
        post_order(T->right);
    }
    printf("%c", T->c);
}

Node * build(int s1, int e1, int s2, int e2){
    Node * res = craete();
    res->c = str1[s1];
    int root_idx;
    for(int i = s2; i <= e2; i++){
        if(str1[s1] == str2[i]){
            root_idx = i;
            break;
        }
    }
    if(root_idx != s2){
        res->left = build(s1 + 1, s1 + (root_idx - s2), s2, root_idx - 1);
    }
    if(root_idx != e2){
        res->right = build(s1 + (root_idx - s2) + 1, e1, root_idx + 1, e2);
    }
    return res;
}

int main(){
    while(scanf("%s", str1) != EOF){
        scanf("%s", str2);
        loc = 0;
        int l1 = strlen(str1);
        int l2 = strlen(str2);
        Node * root = build(0, l1 - 1, 0, l2 - 1);
        post_order(root);
        printf("\n");
    }
    return 0;
}