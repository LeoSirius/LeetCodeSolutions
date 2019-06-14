#include<iostream>
#include<string>
using namespace std;

struct Node{
    Node * left;
    Node * right;
    char v;
}Tree[100];
int loc;

Node * create(){
    Tree[loc].left = Tree[loc].right = NULL;
    return &Tree[loc++];
}

Node * insert(Node * T, char x){
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

char origin_traverse[25], new_traverse[25];
char * tmp_str;
int tmp_size;

void pre_order(Node * T){
    if(T == NULL)
        return;
    tmp_str[tmp_size++] = T->v;
    pre_order(T->left);
    pre_order(T->right);
}

void in_order(Node * T){
    if(T == NULL)
        return;
    in_order(T->left);
    tmp_str[tmp_size++] = T->v;
    in_order(T->right);
}

int main(){
    int n;
    char input_str[11];
    while(scanf("%d", &n) != EOF && n != 0){
        loc = 0;
        Node * T = NULL;
        scanf("%s", input_str);
        for(int i = 0; input_str[i]; i++){
            T = insert(T, input_str[i]);
        }

        //把原始字符串生成的BST的遍历结果保存在origin_traverse中
        tmp_str = origin_traverse;
        pre_order(T);
        in_order(T);
        tmp_size = 0;
        puts(origin_traverse);

        
        // 输入其他n个字符串
        while(n--){
            scanf("%s", input_str);
            Node * new_T = NULL;
            for(int i = 0; input_str[i]; i++){
                new_T = insert(new_T, input_str[i]);
            }

            //把新生成的BST的遍历结果保存到new_traverse中
            tmp_str = new_traverse;
            pre_order(T);
            in_order(T);
            tmp_size = 0;
            puts(new_traverse);
            puts(strcmp(origin_traverse, new_traverse) == 0 ? "YES" : "NO");
        }
    }
    return 0;
}