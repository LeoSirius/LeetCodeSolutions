#include <iostream>
#include "utils_cpp/list.h"
using namespace std;

class Solution {
public:
    ListNode* getKthFromEnd(ListNode* head, int k) {
        ListNode *fast = head, *slow = head;
        while (k--) {
            fast = fast->next;
        }
        while (fast) {
            fast = fast->next;
            slow = slow->next;
        }
        return slow;
    }
};

void test(string test_name, ListNode* head, int k, ListNode* expected)
{
    ListNode* res = Solution().getKthFromEnd(head, k);
    if (is_equal_list(res, expected))
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    ListNode* head1 = new ListNode(1);
    head1->next = new ListNode(2);
    head1->next->next = new ListNode(3);
    head1->next->next->next = new ListNode(4);
    head1->next->next->next->next = new ListNode(5);
    int k1 = 2;
    ListNode* expected1 = new ListNode(4);
    expected1->next = new ListNode(5);
    test("test1", head1, k1, expected1);

    return 0;
}

// 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，
// 即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，
// 它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

// 示例：

// 给定一个链表: 1->2->3->4->5, 和 k = 2.
// 返回链表 4->5.
