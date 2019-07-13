### 思路1 用递归来判断

我们只用判断，不用再生成树本身

```cpp
#include<iostream>
#include<vector>
#include<string>
using namespace std;

bool Judge(vector<int> &tree, vector<int> &obj){
    if(tree.size() == 0 && obj.size() == 0){
        return true;
    }
    // 序列的根必须同
    if(tree.size() != obj.size() || tree[0] != obj[0]){
        return false;
    }

    vector<int> tree_left, tree_right, obj_left, obj_right;
    for(int i = 1; i < tree.size(); ++i){
        if(tree[i] < tree[0]){
            tree_left.push_back(tree[i]);
        }else{
            tree_right.push_back(tree[i]);
        }
        if(obj[i] < obj[0]){
            obj_left.push_back(obj[i]);
        }else{
            obj_right.push_back(obj[i]);
        }
    }
    return Judge(tree_left, obj_left) && Judge(tree_right, obj_right);
}

int main(){
    vector<int> tree, obj;
    string str_tree, str_obj;

    int n;
    while(scanf("%d", &n) != EOF && n){
        cin >> str_tree;
        for(int i = 0; i < str_tree.size(); ++i){
            tree.push_back(str_tree[i] - '0');
        }
        while(n--){
            cin >> str_obj;
            for(int i = 0; i < str_obj.size(); ++i){
                obj.push_back(str_obj[i] - '0');
            }
            if(Judge(tree, obj)){
                cout << "YES" << endl;
            }else{
                cout << "NO" << endl;
            }
        }
    }
    return 0;
}
```