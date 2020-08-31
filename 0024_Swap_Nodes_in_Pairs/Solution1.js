import { ListNode, is_equal_list } from './utils_js/list.js';

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
var swapPairs = function(head) {
  let dummy_head = new ListNode(0);
  dummy_head.next = head;
  let pre = dummy_head;
  let p = head;
  while (p && p.next) {
    let a = p, b = p.next;
    let next = b.next;
    b.next = a;
    a.next = next;
    pre.next = b;

    pre = a;
    p = a.next;
  }
  return dummy_head.next;
};

function test(test_name, head, expected) {
  let res = swapPairs(head);
  if (is_equal_list(res, expected))
    console.log(test_name + ' success.');
  else
    console.log(test_name + ' failed.');
}

let head1 = new ListNode(1);
head1.next = new ListNode(2);
head1.next.next = new ListNode(3);
head1.next.next.next = new ListNode(4);

let expected1 = new ListNode(2);
expected1.next = new ListNode(1);
expected1.next.next = new ListNode(4);
expected1.next.next.next = new ListNode(3);

test('test1', head1, expected1);

let head2 = new ListNode(1);
let expected2 = new ListNode(1);
test('test2', head2, expected2);


// Given a linked list, swap every two adjacent nodes and return its head.

// You may not modify the values in the list's nodes, only nodes itself may be changed.

//  

// Example:

// Given 1->2->3->4, you should return the list as 2->1->4->3.
