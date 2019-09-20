### 思路1 用递归来判断

我们只用判断，不用再生成树本身。为了方便，我们直接在vector中存放字符类型来比较。

```cpp
#include<iostream>
#include<string>
#include<vector>
using namespace std;

bool Judge(vector<char> &tree, vector<char> &obj)
{
    if (tree.size() == 0 && obj.size() == 0) return true;
    // 序列的根必须同
    if (tree.size() != obj.size() || tree[0] != obj[0]) return false;

    vector<char> tree_left, tree_right, obj_left, obj_right;
    for (int i = 1; i < tree.size(); i++) {
        if (tree[i] < tree[0])
            tree_left.push_back(tree[i]);
        else 
            tree_right.push_back(tree[i]);
        if (obj[i] < obj[0])
            obj_left.push_back(obj[i]);
        else 
            obj_right.push_back(obj[i]);
    }
    return Judge(tree_left, obj_left) && Judge(tree_right, obj_right);
}

int main()
{
    int n;
    while (scanf("%d", &n) != EOF && n != 0) {
        string tree_str, obj_str;

        cin >> tree_str;
        vector<char> tree;
        for (int i = 0; tree_str[i]; i++) {
            tree.push_back(tree_str[i]);
        }

        while (n--) {
            vector<char> obj;
            cin >> obj_str;
            for (int i = 0; obj_str[i]; i++) {
                obj.push_back(obj_str[i]);
            }
            if (Judge(tree, obj)) {
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
            }
        }
    }
    return 0;
}

```