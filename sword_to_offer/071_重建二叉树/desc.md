### 题目描述

输入某棵二叉树前序和中序遍历的结果，重建该二叉树。假设输入的前序和中序遍历的结果都不包含重复的数字。

### 样例输入

前序遍历`{1, 2, 4, 7, 3, 5, 6, 8}`，中序遍历`{4, 7, 2, 1, 5, 3, 8, 6}`

### 样例输出

返回重建好的二叉树的根结点。

### 初始代码

```cpp
// struct BinaryTreeNode
// {
//     int m_nValue;
//     BinaryTreeNode *m_pLeft;
//     BinaryTreeNode *m_pRight;
// }
class Solution{
public:
BinaryTreeNode* Construct(int* preorder, int* inorder, int length)
{
}
};
```

### 待改造：把测试用例改成和expected的后续遍历进行比较
