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
        if(lists.empty()){
            return nullptr;
        }
        while(lists.size() >= 2){
            lists.push_back(mergeTwoLists(lists[0], lists[1]));
            lists.erase(lists.begin());
            lists.erase(lists.begin());
        }
        return lists[0];
    }

    // 使用原来的结点merge，没有创建新的结点
    ListNode* mergeTwoLists(ListNode *l1, ListNode *l2){
        ListNode dummy_head = ListNode(0);
        ListNode *p = &dummy_head;
        while(l1 && l2){
            if(l1->val < l2->val){
                p->next = l1;
                l1 = l1->next;
            }else{
                p->next = l2;
                l2 = l2->next;
            }
            p = p->next;
        }
        if(l1){
            p->next = l1;
        }
        if(l2){
            p->next = l2;
        }
        return dummy_head.next;
    }
};