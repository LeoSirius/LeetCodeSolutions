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
 * @param {number} x
 * @return {ListNode}
 */
var partition = function(head, x) {
  let dummy1 = new ListNode(0);
  let dummy2 = new ListNode(0);
  let p1 = dummy1, p2 = dummy2;
  let p = head;
  while (p) {
    if (p.val < x) {
      p1.next = p;
      p1 = p1.next;
    } else {
      p2.next = p;
      p2 = p2.next;
    }
    p = p.next;
  }
  p1.next = dummy2.next;
  p2.next = null;     // 这里必须置空
  return dummy1.next;
};

function test(testName, head, x, expected) {
  let res = partition(head, x);
  if (ListUtils.isEqualList(res, expected))
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}

let head1 = ListUtils.buildList([1,4,3,2,5,2]);
let x1 = 3;
let expeceted1 = ListUtils.buildList([1,2,2,4,3,5]);
test('test1', head1, x1, expeceted1);


// Given a linked list and a value x, partition it such that all
// nodes less than x come before nodes greater than or equal to x.

// You should preserve the original relative order of the nodes in each of the two partitions.

// Example:

// Input: head = 1->4->3->2->5->2, x = 3
// Output: 1->2->2->4->3->5
