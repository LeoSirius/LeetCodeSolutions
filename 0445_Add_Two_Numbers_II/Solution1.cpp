#include <iostream>
#include <stack>
#include "utils_cpp/list.h"
using namespace std;

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> stk1, stk2;
        while (l1) {
            stk1.push(l1->val);
            l1 = l1->next;
        }
        while (l2) {
            stk2.push(l2->val);
            l2 = l2->next;
        }
        int carry = 0;
        ListNode *right = nullptr;
        while (!stk1.empty() || !stk2.empty() || carry) {
            int v1 = 0, v2 = 0;
            if (!stk1.empty()) {
                v1 = stk1.top(); stk1.pop();
            }
            if (!stk2.empty()) {
                v2 = stk2.top(); stk2.pop();
            }
            int sum = v1 + v2 + carry;
            carry = sum / 10;
            ListNode *p = new ListNode(sum % 10);
            p->next = right;
            right = p;
        }
        return right;
    }
};

void test(string test_name, ListNode* l1, ListNode *l2, ListNode* expected)
{
    ListNode* res = Solution().addTwoNumbers(l1, l2);
    if (is_same_list(res, expected))
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}

int main()
{
    ListNode *l11 = new ListNode(7), *l21 = new ListNode(5);
    l11->next = new ListNode(2);
    l11->next->next = new ListNode(4);
    l11->next->next->next = new ListNode(3);
    l21->next = new ListNode(6);
    l21->next->next = new ListNode(4);
    ListNode *expected1 = new ListNode(7);
    expected1->next = new ListNode(8);
    expected1->next->next = new ListNode(0);
    expected1->next->next->next = new ListNode(7);
    test("test1", l11, l21, expected1);

    return 0;
}
