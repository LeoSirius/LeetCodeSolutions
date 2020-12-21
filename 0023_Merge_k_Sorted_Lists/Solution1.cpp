#include <iostream>
#include <vector>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
    ListNode* merge_two(ListNode* a, ListNode *b)
    {
        ListNode *head = new ListNode(0);
        ListNode *p = head;
        while (a && b) {
            if (a->val < b->val) {
                p->next = a;
                a = a->next;
            } else {
                p->next = b;
                b = b->next;
            }
            p = p->next;
        }
        p->next = a ? a : b;
        return head->next;
    }
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode *res = nullptr;
        for (auto head : lists) {
            res = merge_two(res, head);
        }
        return res;
    }
};

void test(string test_name, vector<ListNode*>& lists, ListNode *expected)
{
    ListNode* res = Solution().mergeKLists(lists);
    ListNode* p1 = res;
    ListNode* p2 = expected;
    bool passed = true;
    while (p1 && p2) {
        if (p1->val != p2->val) passed = false;
        if (p1->next == nullptr && p2->next != nullptr) passed = false;
        if (p1->next != nullptr && p2->next == nullptr) passed = false;
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
    ListNode *n1 = new ListNode(1);
    n1->next = new ListNode(4);
    n1->next->next = new ListNode(5);
    ListNode *n2 = new ListNode(1);
    n2->next = new ListNode(3);
    n2->next->next = new ListNode(4);
    ListNode *n3 = new ListNode(2);
    n3->next = new ListNode(6);
    vector<ListNode*> lists1 = {n1, n2, n3};

    ListNode *expected1 = new ListNode(1);
    expected1->next = new ListNode(1);
    expected1->next->next = new ListNode(2);
    expected1->next->next->next = new ListNode(3);
    expected1->next->next->next->next = new ListNode(4);
    expected1->next->next->next->next->next = new ListNode(4);
    expected1->next->next->next->next->next->next = new ListNode(5);
    expected1->next->next->next->next->next->next->next = new ListNode(6);

    test("test1", lists1, expected1);

    vector<ListNode*> lists2;
    ListNode *expected2 = nullptr;
    test("test2", lists2, expected2);

    return 0;
}
