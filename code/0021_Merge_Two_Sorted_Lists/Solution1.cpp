#include <iostream>
#include "utils_cpp/list.h"
using namespace std;


class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *dummy_head = new ListNode(-1);
        ListNode *p = dummy_head;
        while (l1 || l2) {
            int v1, v2;
            v1 = l1 ? l1->val : INT_MAX;
            v2 = l2 ? l2->val : INT_MAX;
            if (v1 < v2) {
                p->next = l1;
                l1 = l1->next;
            } else {
                p->next = l2;
                l2 = l2->next;
            }
            p = p->next;
        }
        return dummy_head->next;
    }
};

void test(string test_name, ListNode* l1, ListNode* l2, ListNode* expected)
{
    ListNode* res = Solution().mergeTwoLists(l1, l2);
    if (is_equal_list(res, expected))
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    ListNode *l11 = new ListNode(1);
    l11->next = new ListNode(2);
    l11->next->next = new ListNode(4);

    ListNode *l21 = new ListNode(1);
    l21->next = new ListNode(3);
    l21->next->next = new ListNode(4);

    ListNode *expected1 = new ListNode(1);
    expected1->next = new ListNode(1);
    expected1->next->next = new ListNode(2);
    expected1->next->next->next = new ListNode(3);
    expected1->next->next->next->next = new ListNode(4);
    expected1->next->next->next->next->next = new ListNode(4);

    // 输入：1->2->4, 1->3->4
    // 输出：1->1->2->3->4->4
    test("test1", l11, l21, expected1);

    return 0;
}

// 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

// 示例1：
// 输入：1->2->4, 1->3->4
// 输出：1->1->2->3->4->4

// 限制：
// 0 <= 链表长度 <= 1000

