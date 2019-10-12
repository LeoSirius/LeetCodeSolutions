#include "../Utilities/List.h"
#include <iostream>
#include <stack>
using namespace std;

// class Solution{
// public:
//     void PrintListReversingly(ListNode* pHead)
//     {
//     }
// };

class Solution{
public:
    void PrintListReversingly(ListNode* pHead)
    {
        stack<int> stk;
        ListNode *p = pHead;
        while (p) {
            stk.push(p->m_nValue);
            p = p->m_pNext;
        }
        while (!stk.empty()) {
            cout << stk.top() << " ";
            stk.pop();
        }
    }
};

// ====================测试代码====================
void Test(ListNode* pHead)
{
    Solution s;
    PrintList(pHead);
    //s.PrintListReversingly_Iteratively(pHead);
    s.PrintListReversingly(pHead);
    printf("\n");
    //s.PrintListReversingly_Recursively(pHead);
}

// 1->2->3->4->5
void Test1()
{
    printf("\nTest1 begins.\n");

    ListNode* pNode1 = CreateListNode(1);
    ListNode* pNode2 = CreateListNode(2);
    ListNode* pNode3 = CreateListNode(3);
    ListNode* pNode4 = CreateListNode(4);
    ListNode* pNode5 = CreateListNode(5);

    ConnectListNodes(pNode1, pNode2);
    ConnectListNodes(pNode2, pNode3);
    ConnectListNodes(pNode3, pNode4);
    ConnectListNodes(pNode4, pNode5);

    Test(pNode1);

    DestroyList(pNode1);
}

// 只有一个结点的链表: 1
void Test2()
{
    printf("\nTest2 begins.\n");

    ListNode* pNode1 = CreateListNode(1);

    Test(pNode1);

    DestroyList(pNode1);
}

// 空链表
void Test3()
{
    printf("\nTest3 begins.\n");

    Test(nullptr);
}

int main(int argc, char* argv[])
{
    Test1();
    Test2();
    Test3();

    return 0;
}