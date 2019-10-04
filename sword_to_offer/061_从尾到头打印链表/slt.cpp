class Solution{
public:
void PrintListReversingly_Iteratively(ListNode* pHead)
{
    stack<ListNode *> nodes;
    ListNode *pNode = pHead;
    while (pNode != nullptr) {
        nodes.push(pNode);
        pNode = pNode->m_pNext;
    }
    while (!nodes.empty()) {
        pNode = nodes.top();
        nodes.pop();
        printf("%d ", pNode->m_nValue);
    }
}
void PrintListReversingly_Recursively(ListNode* pHead)
{
    if(pHead != nullptr)
    {
        if (pHead->m_pNext != nullptr)
        {
            PrintListReversingly_Recursively(pHead->m_pNext);
        }
 
        printf("%d\t", pHead->m_nValue);
    }
}
};