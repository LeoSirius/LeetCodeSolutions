#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode *head = new ListNode(0);
        ListNode *p = head;
        while (l1 || l2 || carry) {
            int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
            carry = sum / 10;
            p->next = new ListNode(sum % 10);
            p = p->next;
            l1 = l1 ? l1->next : l1;
            l2 = l2 ? l2->next : l2;
        }
        return head->next;
    }
};

void test(string test_name, ListNode *l1, ListNode *l2, ListNode *expected) {
    // 测试方法：把链表的每一项写到一个vector，再比较vector

    Solution s;
    ListNode *res = s.addTwoNumbers(l1, l2);
    ListNode *p = res;
    vector<int> res_nums;
    vector<int> expected_nums;
    while (p) {
        res_nums.push_back(p->val);
        p = p->next;
    }
    p = expected;
    while (p) {
        expected_nums.push_back(p->val);
        p = p->next;
    }
    if (res_nums == expected_nums) {
        cout << test_name << " success." << endl;
    } else {
        cout << test_name << " failed." << endl;
    }
}

int main()
{
    ListNode *a1 = new ListNode(2);
    ListNode *a2 = new ListNode(4);
    ListNode *a3 = new ListNode(3);
    a1->next = a2;
    a2->next = a3;
    ListNode *b1 = new ListNode(5);
    ListNode *b2 = new ListNode(6);
    ListNode *b3 = new ListNode(4);
    b1->next = b2;
    b2->next = b3;

    ListNode *c1 = new ListNode(7);
    ListNode *c2 = new ListNode(0);
    ListNode *c3 = new ListNode(8);
    c1->next = c2;
    c2->next = c3;
    // 2->4->3 + 5->6->4 = 7->0->8
    test("test1", a1, b1, c1);

    return 0;
}
