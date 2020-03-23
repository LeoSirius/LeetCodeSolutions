#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode *fast, *slow;
        fast = slow = head;
        while (fast) {
            fast = fast->next;
            if (!fast)
                return slow;
            slow = slow->next;
            fast = fast->next;
            if (!fast)
                return slow;
        }
        return slow;
    }
};


void test(string test_name, ListNode* head, ListNode* expected)
{
    ListNode* res = Solution().middleNode(head);
    if (res->val == expected->val) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    ListNode *head1 = new ListNode(1);
    head1->next = new ListNode(2);
    head1->next->next = new ListNode(3);
    head1->next->next->next = new ListNode(4);
    head1->next->next->next->next = new ListNode(5);
    ListNode *expected1 = new ListNode(3);
    test("test1", head1, expected1);

    ListNode *head2 = new ListNode(1);
    head2->next = new ListNode(2);
    head2->next->next = new ListNode(3);
    head2->next->next->next = new ListNode(4);
    head2->next->next->next->next = new ListNode(5);
    head2->next->next->next->next->next = new ListNode(6);
    ListNode *expected2 = new ListNode(4);
    test("test2", head2, expected2);

    return 0;
}
