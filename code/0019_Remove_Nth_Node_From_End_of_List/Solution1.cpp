#include <iostream>
#include "utils_cpp/list.h"
using namespace std;

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *dummy = new ListNode(-1);
        dummy->next = head;
        ListNode *fast = head, *slow = head;
        while (n-- && fast) {
            fast = fast->next;
        }

        // n保证了是合法的。这里如果没有fast，表示n == 链表长度。所以跳过第一个就可以了
        if (!fast) {
            return dummy->next->next;
        }
        while (fast->next) {
            fast = fast->next;
            slow = slow->next;
        }
        slow->next = slow->next->next;
        return dummy->next;
    }
};

void test(string test_name, ListNode* head, int n, ListNode* expected)
{
    ListNode* res = Solution().removeNthFromEnd(head, n);
    if (is_equal_list(res, expected))
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    ListNode *list1 = new ListNode(1);
    list1->next = new ListNode(2);
    list1->next->next = new ListNode(3);
    list1->next->next->next = new ListNode(4);
    list1->next->next->next->next = new ListNode(5);
    int n1 = 2;
    ListNode *expected1 = new ListNode(1);
    expected1->next = new ListNode(2);
    expected1->next->next = new ListNode(3);
    expected1->next->next->next = new ListNode(5);
    test("test1", list1, n1, expected1);

    ListNode *list2 = new ListNode(1);
    int n2 = 1;
    ListNode *expected2 = nullptr;
    test("test2", list2, n2, expected2);

    ListNode *list3 = new ListNode(1);
    list3->next = new ListNode(2);
    int n3 = 2;
    ListNode *expected3 = new ListNode(2);
    test("test3", list3, n3, expected3);

    return 0;
}

// Given a linked list, remove the n-th node from the end of list 
// and return its head.

// Example:

// Given linked list: 1->2->3->4->5, and n = 2.

// After removing the second node from the end, the linked list
//  becomes 1->2->3->5.

// Note:

// Given n will always be valid.

// Follow up:

// Could you do this in one pass?

