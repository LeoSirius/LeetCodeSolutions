
## 思路1 利用生成树的遍历序列


两棵树前序、中序的遍历结果都一样，就是同一棵树。我们把遍历的结果放在字符串中保存，然后比较字符串。另外在遍历中，我们可以先判断传入的结点是否为空，这样就不用在遍历左右子树的时候都判断一下。

```cpp
#include<iostream>
#include<string>
#include<vector>

using namespace std;

struct Node{
    Node * left;
    Node * right;
    int v;
};

vector<int> origin_traverse, new_traverse;

Node * create(){
    Node * tmp_node = new Node();
    tmp_node->left = tmp_node->right = nullptr;
    return tmp_node;
}

Node * insert(Node * T, int v){
    if(T == nullptr){
        T = create();
        T->v = v;
        return T;
    }else if(v < T->v){
        T->left = insert(T->left, v);
    }else{
        T->right = insert(T->right, v);
    }
    return T;
}

void pre_order(Node * T, bool is_new){
    if(T == nullptr)
        return;
    if(is_new){
        new_traverse.push_back(T->v);
    }else{
        origin_traverse.push_back(T->v);
    }
    pre_order(T->left, is_new);
    pre_order(T->right, is_new);
}

void in_order(Node * T, bool is_new){
    if(T == nullptr)
        return;
    pre_order(T->left, is_new);
    if(is_new){
        new_traverse.push_back(T->v);
    }else{
        origin_traverse.push_back(T->v);
    }
    pre_order(T->right, is_new);
}

int main(){
    int n;
    string input_str;
    while(scanf("%d", &n) != EOF && n != 0){
        if(origin_traverse.size())
            origin_traverse.clear();
        if(new_traverse.size())
            new_traverse.clear();

        cin >> input_str;
        Node * origin_tree = new Node();
        for(int i = 0; i < input_str.size(); i++){
            origin_tree = insert(origin_tree, input_str[i]);
        }
        pre_order(origin_tree, false);
        in_order(origin_tree, false);

        while(n--){
            cin >> input_str;
            Node * new_tree = new Node();
            for(int i = 0; i < input_str.size(); i++){
                new_tree = insert(new_tree, input_str[i]);
            }
            pre_order(new_tree, true);
            in_order(new_tree, true);

            bool is_same = false;
            if(origin_traverse.size() == new_traverse.size()){
                int i = 0;
                for(; i < origin_traverse.size(); i++){
                    if(origin_traverse[i] != new_traverse[i])
                        break;
                }
                if(i == origin_traverse.size())
                    is_same = true;
            }
            if(is_same)
                cout << "YES" << endl;
            else
                cout << "NO" << endl;
        }
    }
    return 0;
}
```