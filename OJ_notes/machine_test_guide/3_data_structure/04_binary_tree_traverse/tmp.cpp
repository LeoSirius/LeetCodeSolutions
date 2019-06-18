#include<iostream>
#include<string>
using namespace std;

struct Node{
    Node * left;
    Node * right;
    char v;
};

string pre_str, in_str;

Node * create(){
    Node * Tree = new Node();
    Tree->left = Tree->right = NULL;
    return Tree;
}

Node * BuildTree(int s1, int e1, int s2, int e2){
    Node * tmp_node = create();
    tmp_node->v = pre_str[s1];
    int root_idx = s2;
    for(int i = s2; i <= e2; i++){
        if(pre_str[s1] == in_str[i]){
            root_idx = i;
            break;
        }
    }
    if(root_idx != s2){
        tmp_node->left = BuildTree(s1+1, s1 + (root_idx - s2), s2, root_idx - 1);
    }
    if(root_idx != e2){
        tmp_node->right = BuildTree(s1 + (root_idx - s2) + 1, e1, root_idx + 1, e2);
    }
    return tmp_node;
}

void post_order(Node * Tree){
    if(Tree == NULL)
        return;
    post_order(Tree->left);
    post_order(Tree->right);
    printf("%c", Tree->v);
}

int main(){
    while(cin >> pre_str){
        cin >> in_str;
        int length = pre_str.length();
        Node * Tree = BuildTree(0, length - 1, 0, length - 1);
        post_order(Tree);
        printf("\n");
    }
    return 0;
}