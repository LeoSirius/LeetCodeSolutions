#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;

        ListNode *dummy_head = new ListNode(0);
        ListNode *l, *r, *pre, *cur, *jump;

        dummy_head->next = head;
        jump = dummy_head;
        l = r = head;

        while (true) {
            int cnt = 0;
            while (r && cnt < k) {
                r = r->next;
                ++cnt;
            }
            
            if (cnt == k) {
                // l is current group's first node
                // after this while, r point to (k+1)th node
                // which is next group's frist node
                pre = r;
                cur = l;
                // 下面这个while把l到r之间的node反转。
                while (cnt--) {
                    ListNode *tmp = cur->next;
                    cur->next = pre;
                    pre = cur;
                    cur = tmp;
                }
                jump->next = pre;
                jump = l;   // l is right most node after reverse
                l = r;      // // l point to next group's first node
            } else {
                return dummy_head->next;
            }
        }
    }
};

void test(string test_name, ListNode* head, int k, ListNode* expected)
{
    ListNode *p1 = Solution().reverseKGroup(head, k);
    ListNode *p2 = expected;
    bool passed = true;
    while (p1 || p2) {
        if (!p1 || !p2) {
            passed = false;
            break;
        }
        if (p1->val != p2->val) {
            passed = false;
            break;
        }
        p1 = p1->next;
        p2 = p2->next;
    }

    if (passed) {
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

    int k1 = 2;
    ListNode *expected1 = new ListNode(2);
    expected1->next = new ListNode(1);
    expected1->next->next = new ListNode(4);
    expected1->next->next->next = new ListNode(3);
    expected1->next->next->next->next = new ListNode(5);
    test("test1", head1, k1, expected1);

    ListNode *head2 = new ListNode(1);
    head2->next = new ListNode(2);
    head2->next->next = new ListNode(3);
    head2->next->next->next = new ListNode(4);
    head2->next->next->next->next = new ListNode(5);
    int k2 = 3;
    ListNode *expected2 = new ListNode(3);
    expected2->next = new ListNode(2);
    expected2->next->next = new ListNode(1);
    expected2->next->next->next = new ListNode(4);
    expected2->next->next->next->next = new ListNode(5);
    test("test2", head2, k2, expected2);

    return 0;
}
