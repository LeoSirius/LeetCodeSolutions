#include "list.h"

bool is_equal_list(ListNode *l1, ListNode *l2)
{
    while (true) {
        if (!l1 && !l2)
            return true;
        if (!l1 || !l2)
            return false;
        if (l1->val != l2->val)
            return false;
        l1 = l1 ? l1->next : l1;
        l2 = l2 ? l2->next : l2;
    }
}