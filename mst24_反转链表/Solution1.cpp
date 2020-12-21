#include <iostream>
#include "utils_cpp/list.h"
using namespace std;


class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode *pre = nullptr, *cur = head, *next = nullptr;
        while (cur) {
            next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }
        return pre;
    }
};

void test(string test_name, ListNode* head, ListNode* expected)
{
    ListNode *res = Solution().reverseList(head);
    if (is_equal_list(res, expected))
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    ListNode *head1 = new ListNode(1);
    head1->next = new ListNode(2);
    head1->next->next = new ListNode(3);
    head1->next->next->next = new ListNode(4);
    head1->next->next->next->next = new ListNode(5);

    ListNode *expected1 = new ListNode(5);
    expected1->next = new ListNode(4);
    expected1->next->next = new ListNode(3);
    expected1->next->next->next = new ListNode(2);
    expected1->next->next->next->next = new ListNode(1);
    test("test1", head1, expected1);

    ListNode *head2 = nullptr;
    ListNode *expected2 = nullptr;
    test("test2", head2, expected2);

    return 0;
}

// 定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

// 示例:
// 输入: 1->2->3->4->5->NULL
// 输出: 5->4->3->2->1->NULL
//  

// 限制：
// 0 <= 节点个数 <= 5000

