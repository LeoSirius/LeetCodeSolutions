#include <iostream>
#include "utils_cpp/list.h"
using namespace std;


class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        if (!head) return nullptr;
        if (!k) return head;

        ListNode *last = head;
        int len = 1;
        while (last->next) {
            last = last->next;
            len++;
        }
        last->next = head;

        k %= len;
        // 1,2,3,4,5,6,7
        // 6,7,1,2,3,4,5
        // new_right_len = 5, p 从7移动5步到5.再从5断开就行了
        ListNode *p = last;
        int new_right_len = len - k;
        while (new_right_len--) {
            p = p->next;
        }
        ListNode *res = p->next;
        p->next = nullptr;
        return res;
    }
};

void test(string test_name, ListNode* head, int k, ListNode* expected)
{
    ListNode *res = Solution().rotateRight(head, k);
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
    int k1 = 2;
    ListNode *expected1 = new ListNode(4);
    expected1->next = new ListNode(5);
    expected1->next->next = new ListNode(1);
    expected1->next->next->next = new ListNode(2);
    expected1->next->next->next->next = new ListNode(3);
    test("test1", head1, k1, expected1);

    ListNode *head2 = new ListNode(0);
    head2->next = new ListNode(1);
    head2->next->next = new ListNode(2);
    int k2 = 4;
    ListNode *expected2 = new ListNode(2);
    expected2->next = new ListNode(0);
    expected2->next->next = new ListNode(1);
    test("test2", head2, k2, expected2);

    ListNode *head3 = nullptr;
    int k3 = 0;
    ListNode *expected3 = nullptr;
    test("test3", head3, k3, expected3);

    ListNode *head4 = new ListNode(1);
    head4->next = new ListNode(2);
    int k4 = 0;
    ListNode *expected4 = new ListNode(1);
    expected4->next = new ListNode(2);
    test("test4", head4, k4, expected4);

    ListNode *head5 = new ListNode(1);
    head5->next = new ListNode(2);
    int k5 = 1;
    ListNode *expected5 = new ListNode(2);
    expected5->next = new ListNode(1);
    test("test5", head5, k5, expected5);

    return 0;
}

// Given a linked list, rotate the list to the right by k places,
//  where k is non-negative.

// Example 1:

// Input: 1->2->3->4->5->NULL, k = 2
// Output: 4->5->1->2->3->NULL
// Explanation:
// rotate 1 steps to the right: 5->1->2->3->4->NULL
// rotate 2 steps to the right: 4->5->1->2->3->NULL
// Example 2:

// Input: 0->1->2->NULL, k = 4
// Output: 2->0->1->NULL
// Explanation:
// rotate 1 steps to the right: 2->0->1->NULL
// rotate 2 steps to the right: 1->2->0->NULL
// rotate 3 steps to the right: 0->1->2->NULL
// rotate 4 steps to the right: 2->0->1->NULL

