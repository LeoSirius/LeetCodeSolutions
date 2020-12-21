#include <iostream>
#include <queue>
#include "utils_cpp/tree.h"
using namespace std;

class Codec {
public:

    // Encodes a tree to a single string.
    string serialize(TreeNode* root) {
        // 注意这种层序遍历的方法会在每个子节点后面都加两个null
        // 但是只要能序列化回去就行。题目没有直接规定序列化后的内容
        string res = "";
        queue<TreeNode*> que;
        if (!root) return res; 

        que.push(root);
        while (!que.empty()) {
            TreeNode *p = que.front(); que.pop();

            if (p) {
                res += to_string(p->val) + ",";
                que.push(p->left);
                que.push(p->right);
            } else {
                res += "null,";
            }
        }
        res.pop_back();
        return res;
    }

    // Decodes your encoded data to tree.
    TreeNode* deserialize(string data) {
        TreeNode *dummy = new TreeNode(0);
        queue<TreeNode*> que;
        que.push(dummy);

        size_t beg = 0, end = 0;  // 左闭右开
        bool left_child = false;   // 把根结点作为dummy的右节点。之后left_child=true。正好加第一个左节点

        while (beg < data.size()) {
            while (end < data.size() && data[end] != ',') end++;

            string str = data.substr(beg, end - beg);
            TreeNode *node = nullptr;
            if (str != "null") node = new TreeNode(atoi(str.c_str()));

            TreeNode *p = que.front();
            if (left_child) {
                p->left = node;
            } else {
                p->right = node;
                que.pop();
            }

            if (node) que.push(node);
            left_child = !left_child;
            beg = ++end;
        }
        return dummy->right;
    }
};

void test1()
{
    //     1
    //    / \
    //   2   3
    //      / \
    //     4   5

    // 序列化为 "[1,2,3,null,null,4,5]"
    TreeNode *tree = new TreeNode(1);
    tree->left = new TreeNode(2);
    tree->right = new TreeNode(3);
    tree->right->left = new TreeNode(4);
    tree->right->right = new TreeNode(5);
    Codec codec;
    string serialized = codec.serialize(tree);
    cout << "serialized = " + serialized << endl;
    TreeNode *res_tree = codec.deserialize(serialized);
    if (is_equal_tree(res_tree, tree))
        cout << "test1 success." << endl;
    else
        cout << "test1 failed." << endl;
}

int main()
{
    test1();

    return 0;
}

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.deserialize(codec.serialize(root));

// 请实现两个函数，分别用来序列化和反序列化二叉树。

// 示例: 

// 你可以将以下二叉树：

//     1
//    / \
//   2   3
//      / \
//     4   5

// 序列化为 "[1,2,3,null,null,4,5]"

