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
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
  let p = head;
  while (p && p.next) {
    while (p.next && p.val == p.next.val) {
      p.next = p.next.next;
    }
    p = p.next;
  }
  return head;
};

function test(testName, head, expected) {
  let res = deleteDuplicates(head);
  if (ListUtils.isEqualList(res, expected))
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}

let head1 = ListUtils.buildList([1,2,2,]);
let expected1 = ListUtils.buildList([1,2]);
test('test1', head1, expected1);

let head2 = ListUtils.buildList([1,1,1,2,3]);
let expected2 = ListUtils.buildList([1,2,3]);
test('test2', head2, expected2);


// Given a sorted linked list, delete all duplicates such that each element appear only once.

// Example 1:

// Input: 1->1->2
// Output: 1->2
// Example 2:

// Input: 1->1->2->3->3
// Output: 1->2->3