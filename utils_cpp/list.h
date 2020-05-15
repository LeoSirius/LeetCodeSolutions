#include <iostream>
// using namespace std;

#ifndef LIST_H
#define LIST_H

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

bool is_same_list(ListNode* l1, ListNode* l2);

#endif