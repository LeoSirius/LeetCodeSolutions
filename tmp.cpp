/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode head(0);
        ListNode *p = &head;
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
        return head.next;
    }
};