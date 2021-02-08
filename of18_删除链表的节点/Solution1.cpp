#include <iostream>
#include "utils_cpp/list.h"
using namespace std;

class Solution {
public:
    ListNode* deleteNode(ListNode* head, int val) {
        ListNode *dummy_head = new ListNode(-1);
        dummy_head->next = head;
        ListNode *p = dummy_head;

        while (p->next) {
            if (p->next->val == val) {
                p->next = p->next->next;
                break;
            }
            p = p->next;
        }
        return dummy_head->next;
    }
};


void test(string test_name, ListNode* head, int val, ListNode* expected)
{
    ListNode *res = Solution().deleteNode(head, val);
    if (is_equal_list(res, expected))
        cout << test_name << " success." << endl;
    else
        cout << test_name << " failed." << endl;
}


int main()
{
    ListNode *head1 = new ListNode(4);
    head1->next = new ListNode(5);
    head1->next->next = new ListNode(1);
    head1->next->next->next = new ListNode(9);
    int val1 = 5;
    ListNode *expected1 = new ListNode(4);
    expected1->next = new ListNode(1);
    expected1->next->next = new ListNode(9);
    test("test1", head1, val1, expected1);

    ListNode *head2 = new ListNode(4);
    head2->next = new ListNode(5);
    head2->next->next = new ListNode(1);
    head2->next->next->next = new ListNode(9);
    int val2 = 1;
    ListNode *expected2 = new ListNode(4);
    expected2->next = new ListNode(5);
    expected2->next->next = new ListNode(9);
    test("test2", head2, val2, expected2);

    return 0;
}

// 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

// 返回删除后的链表的头节点。

// 注意：此题对比原题有改动

// 说明：

// 题目保证链表中节点的值互不相同
// 若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点

// 示例 1:

// 输入: head = [4,5,1,9], val = 5
// 输出: [4,1,9]
// 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.


// 示例 2:

// 输入: head = [4,5,1,9], val = 1
// 输出: [4,5,9]
// 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
//  

// 说明：

// 题目保证链表中节点的值互不相同
// 若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点
