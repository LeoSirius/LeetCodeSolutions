### 思路1 生成一个二叉树，在后序遍历

```cpp
#include<iostream>
#include<string>
using namespace std;

struct Node{
    Node *left;
    Node *right;
    char v;
};
char str1[27], str2[27];    // 声明两个字符数组，分别保存输入的前序和中序遍历

Node *create(){
    // 申请一个结点空间，返回指向其的指针
    Node *node = new Node();
    node->left = node->right = nullptr;
    return node;
}

void postorder(Node *T){
    if(T == nullptr){
        return;
    }
    postorder(T->left);
    postorder(T->right);
    printf("%c", T->v);
}

Node *build(int s1, int e1, int s2, int e2){
    Node *node = create();
    node->v = str1[s1];
    int root_index;
    for(int i = s2; i <= e2; ++i){
        if(str1[s1] == str2[i]){
            root_index = i;
            break;
        }
    }
    // 下面分别先检查左右子树不为空，再进行构建
    if(root_index != s2){
        node->left = build(s1+1, s1+(root_index-s2), s2, root_index-1);
    }
    if(root_index != e2){
        node->right = build(s1+(root_index-s2)+1, e1, root_index+1, e2);
    }
    return node;
}

int main(){
    while(scanf("%s %s", str1, str2) == 2){
        int size = strlen(str1);
        Node *T = build(0, size-1, 0, size-1);
        postorder(T);
        printf("\n");
    }
    return 0;
}
```