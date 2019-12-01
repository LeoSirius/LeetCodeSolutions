### 题目描述

给定一个二叉树和其中一个节点，输出中序遍历中的下一个节点。给出的节点结构除了分别指向左右子节点的指针，还有一个指向父节点的指针。

### 样例输入

            8
        6      10
       5 7    9  11

二叉树结构如上，输入指向节点7的指针

### 样例输出

返回指向8的指针

### 初始代码

```cpp
// struct BinaryTreeNode
// {
//     int                    m_nValue;
//     BinaryTreeNode*        m_pLeft;
//     BinaryTreeNode*        m_pRight;
//     BinaryTreeNode*        m_pParent;
// };
class Solution{
public:
BinaryTreeNode* GetNext(BinaryTreeNode* pNode)
{
}
};
```