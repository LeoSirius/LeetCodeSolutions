#include <iostream>
#include "utils_cpp/tree.h"
using namespace std;

class Solution {
    bool is_sub(TreeNode* t1, TreeNode* t2)
    {
        // 注意这里与is_same_tree的区别
        if (!t2) return true;    // b空，a不管空不空都是true，说明b已经遍历到底了
        if (!t1) return false;   // b不空，但是a已经耗尽，则false
        if (t1->val != t2->val) return false;
        return is_sub(t1->left, t2->left) && is_sub(t1->right, t2->right);
    }
public:
    bool isSubStructure(TreeNode* A, TreeNode* B) {
        if (!A || !B)
            return false;
        return is_sub(A, B) || isSubStructure(A->left, B) || isSubStructure(A->right, B);
    }
};

void test(string test_name, TreeNode* A, TreeNode* B, bool expected)
{
    bool res = Solution().isSubStructure(A, B);
    if (res == expected)
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    // 给定的树 A:
    //      3
    //     / \
    //    4   5
    //   / \
    //  1   2
    TreeNode *A1 = new TreeNode(3);
    A1->left = new TreeNode(4);
    A1->left->left = new TreeNode(1);
    A1->left->right = new TreeNode(2);
    A1->right = new TreeNode(5);

    // 给定的树 B：
    //    4 
    //   /
    //  1
    TreeNode *B1 = new TreeNode(4);
    B1->left = new TreeNode(1);

    bool expected1 = true;
    test("test1", A1, B1, expected1);

    return 0;
}

// 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

// B是A的子结构， 即 A中有出现和B相同的结构和节点值。

// 例如:
// 给定的树 A:

//      3
//     / \
//    4   5
//   / \
//  1   2
// 给定的树 B：

//    4 
//   /
//  1
// 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

// 示例 1：
// 输入：A = [1,2,3], B = [3,1]
// 输出：false

// 示例 2：
// 输入：A = [3,4,5,1,2], B = [4,1]
// 输出：true
// 限制：

// 0 <= 节点个数 <= 10000

