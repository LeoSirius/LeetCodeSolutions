import { ListUtils, ListNode } from './utils_js/list.js';

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
  if (!head || !k)
    return head;
  let length = 0;
  let p = head;
  let old_tail = p;
  while (p) {
    length++;
    old_tail = p;
    p = p.next;
  }

  k %= length;

  // 如果k == length或其倍数，直接返回原链表
  if (!k) {
    return head;
  }

  let new_tail = head;
  let new_tail_step = length - k - 1;
  while (new_tail_step--) {
    new_tail = new_tail.next;
  }
  let new_head = new_tail.next;
  old_tail.next = head;
  new_tail.next = null;
  return new_head;
};

function test(test_name, head, k, expected) {
  let res = rotateRight(head, k);
  if (ListUtils.isEqualList(res, expected))
    console.log(test_name + ' success.');
  else
    console.log(test_name + ' failed.');
}

let head1 = new ListNode(1)
head1.next = new ListNode(2)
head1.next.next = new ListNode(3)
head1.next.next.next = new ListNode(4)
head1.next.next.next.next = new ListNode(5)
let k1 = 2;
let expected1 = new ListNode(4);
expected1.next = new ListNode(5);
expected1.next.next = new ListNode(1);
expected1.next.next.next = new ListNode(2);
expected1.next.next.next.next = new ListNode(3);
test('test1', head1, k1, expected1);

let head2 = new ListNode(0);
head2.next = new ListNode(1);
head2.next.next = new ListNode(2);
let k2 = 4;
let expected2 = new ListNode(2);
expected2.next = new ListNode(0);
expected2.next.next = new ListNode(1);
test('test2', head2, k2, expected2);

let head3 = null;
let k3 = 0;
let expected3 = null;
test('test3', head3, k3, expected3);

let head4 = new ListNode(1);
head4.next = new ListNode(2);
let k4 = 0;
let expected4 = new ListNode(1);
expected4.next = new ListNode(2);
test('test4', head4, k4, expected4);

let head5 = new ListNode(1);
head5.next = new ListNode(2);
let k5 = 1;
let expected5 = new ListNode(2);
expected5.next = new ListNode(1);
test('test5', head5, k5, expected5);

let head6 = new ListNode(1);
let k6 = 1;
let expected6 = new ListNode(1);
test('test6', head6, k6, expected6);


// Given a linked list, rotate the list to the right by k places, where k is non-negative.

// Example 1:

// Input: 1->2->3->4->5->NULL, k = 2
// Output: 4->5->1->2->3->NULL
// Explanation:
// rotate 1 steps to the right: 5->1->2->3->4->NULL
// rotate 2 steps to the right: 4->5->1->2->3->NULL

// Example 2:

// Input: 0->1->2->NULL, k = 4
// Output: 2->0->1->NULL
// Explanation:
// rotate 1 steps to the right: 2->0->1->NULL
// rotate 2 steps to the right: 1->2->0->NULL
// rotate 3 steps to the right: 0->1->2->NULL
// rotate 4 steps to the right: 2->0->1->NULL