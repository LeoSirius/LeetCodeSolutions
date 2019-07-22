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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(head == nullptr || k == 1) return head;
        ListNode *dummy_head = new ListNode(0);
        dummy_head->next = head;
        ListNode *jump = dummy_head;
        ListNode *l, *r, *pre, *cur;

        l = r = head;
        while(true){
            int count = 0;
            while(r && count < k){
                r = r->next;
                count++;
            }
            if(count == k){
                pre = r;
                cur = l;
                while(count--){
                    ListNode *tmp_node = cur->next;
                    cur->next = pre;
                    pre = cur;
                    cur = tmp_node;
                }
                jump->next = pre;
                jump = l;
                l = r;
            }else{
                return dummy_head->next;
            }
        }

    }
};