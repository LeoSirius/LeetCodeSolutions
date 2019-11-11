#include<iostream>
#include<vector>
using namespace std;

bool Judge(vector<char> &tree, vector<char> &obj)
{
    if (tree.size() == 0 && obj.size() == 0) return true;
    if (tree.size() != obj.size() || tree[0] != obj[0]) return false;

    vector<char> tree_left, tree_right, obj_left, obj_right;
    char root = tree[0];
    for (int i = 1; i < tree.size(); i++) {
        if (tree[i] < root)
            tree_left.push_back(tree[i]);
        else
            tree_right.push_back(tree[i]);
        if (obj[i] < root)
            obj_left.push_back(obj[i]);
        else
            obj_right.push_back(obj[i]);
    }
    return Judge(tree_left, obj_left) && Judge(tree_right, obj_right);
}

int main()
{
    int n;
    while (scanf("%d", &n) != EOF && n) {
        string tree_str, obj_str;
        cin >> tree_str;
        vector<char> tree;
        for (int i = 0; tree_str[i]; i++) {
            tree.push_back(tree_str[i]);
        }

        while (n--) {
            cin >> obj_str;
            vector<char> obj;
            for (int i = 0; obj_str[i]; i++) {
                obj.push_back(obj_str[i]);
            }
            if (Judge(tree, obj)) {
                printf("YES\n");
            } else {
                printf("NO\n");
            }
        }
    }
    return 0;
}