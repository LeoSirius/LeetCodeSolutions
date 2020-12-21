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
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
var reverseBetween = function(head, m, n) {
  let dummyHead = new ListNode(0);
  dummyHead.next = head;
  let leftTail = dummyHead, rightHead = null;
  let pm = null, pn = dummyHead;
  m -= 1;
  if (m < 0 || n < 0)
    return head;
  while (m--) {
    leftTail = leftTail.next;
  }
  while (n--) {
    pn = pn.next;
  }
  rightHead = pn.next;
  pn.next = null;
  pm = leftTail.next;

  // now reverse pm to pn
  let dummy = new ListNode(0);
  dummy.next = pm;
  let a = dummy, b = pm, c = pm.next;
  while (b) {
    b.next = a;

    a = b;
    b = c;
    c = c ? c.next : null;
  }

  // seam lists
  pm.next = rightHead;
  leftTail.next = pn;

  return dummyHead.next;
};

function test(testName, head, m, n, expected) {
  let res = reverseBetween(head, m, n);
  if (ListUtils.isEqualList(res, expected))
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}


let head1 = ListUtils.buildList([1,2,3,4,5]);
let m1 = 2, n1 = 4;
let expected1 = ListUtils.buildList([1,4,3,2,5]);
test('test1', head1, m1, n1, expected1);

let head2 = ListUtils.buildList([5]);
let m2 = 1, n2 = 1;
let expected2 = ListUtils.buildList([5]);
test('test2', head2, m2, n2, expected2);

let head3 = ListUtils.buildList([3,5]);
let m3 = 1, n3 = 2;
let expected3 = ListUtils.buildList([5,3]);
test('test3', head3, m3, n3, expected3);


// Reverse a linked list from position m to n. Do it in one-pass.

// Note: 1 ≤ m ≤ n ≤ length of list.

// Example:

// Input: 1->2->3->4->5->NULL, m = 2, n = 4
// Output: 1->4->3->2->5->NULL