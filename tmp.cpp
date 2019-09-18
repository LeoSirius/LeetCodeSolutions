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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode *res = nullptr;
        if (lists.size() == 0) {
            return res;
        } else if (lists.size() == 1) {
            return lists[0];
        }
        while (lists.size() > 1) {
            res = mergeTwo(lists[0], lists[1]);
            lists.erase(lists.begin(), lists.begin()+2);  // vector.erase 很慢
            lists.push_back(res);
        }
        return res;
    }

    ListNode* mergeTwo(ListNode *h1, ListNode *h2)
    {
        ListNode head(0);
        ListNode *l1, *l2, *p;
        p = &head;
        l1 = h1; l2 = h2;
        int v1, v2;
        while (l1 || l2) {
            v1 = l1 ? l1->val : __INT_MAX__;
            v2 = l2 ? l2->val : __INT_MAX__;
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