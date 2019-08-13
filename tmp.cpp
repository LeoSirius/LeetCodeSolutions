#include<iostream>
#include<string>
using namespace std;

struct Node{
    char value;
    Node* left;
    Node* right;
};

string pre_str, in_str;

Node* create_node(){
    Node* new_node = new Node;
    new_node->left = new_node->right = nullptr;
    return new_node;
}

Node* build_tree(int s1, int e1, int s2, int e2){
    int root_idx;
    Node* cur_node = create_node();
    cur_node->value = pre_str[s1];
    for(int i = s2; i <= e2; i++){
        if(pre_str[s1] == in_str[i]){
            root_idx = i;
            break;
        }
    }
    if(root_idx != s2){
        cur_node->left = build_tree(s1+1, s1+(root_idx-s2), s2, root_idx-1);
    }
    if(root_idx != e2){
        cur_node->right = build_tree(s1+(root_idx-s2)+1, e1, root_idx+1, e2);
    }
    return cur_node;
}

void post_order(Node* tree){
    if(tree == nullptr) return;
    post_order(tree->left);
    post_order(tree->right);
    cout << tree->value;
}

int main(){
    while(cin >> pre_str >> in_str){
        int len = pre_str.size();
        Node* tree = build_tree(0, len-1, 0, len-1);
        post_order(tree);
        cout << endl;
    }
    return 0;
}