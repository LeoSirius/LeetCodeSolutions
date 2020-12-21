import { is_equal_list, ListNode } from './utils_js/list.js';

/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
  let fast = head, slow = head;
  let dummy = new ListNode(0);
  dummy.next = head;
  while (n--) {
    fast = fast.next;
  }
  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next;
  }
  if (!fast)
    return dummy.next.next;
  slow.next = slow.next.next;
  return dummy.next;
};


function test(test_name, head, n, expected) {
  let res = removeNthFromEnd(head, n);
  if (is_equal_list(res, expected)) {
    console.log(test_name + ' success.');
  } else {
    console.log(test_name + ' failed.');
  }
}


let list1 = new ListNode(1);
list1.next = new ListNode(2);
list1.next.next = new ListNode(3);
list1.next.next.next = new ListNode(4);
list1.next.next.next.next = new ListNode(5);
let n1 = 2;
let expected1 = new ListNode(1);
expected1.next = new ListNode(2);
expected1.next.next = new ListNode(3);
expected1.next.next.next = new ListNode(5);
test('test1', list1, n1, expected1);

let list2 = new ListNode(1);
let n2 = 1;
let expected2 = null;
test('test2', list2, n2, expected2);

let list3 = new ListNode(1);
list3.next = new ListNode(2);
let n3 = 2;
let expected3 = new ListNode(2);
test('test3', list3, n3, expected3);


// Given a linked list, remove the n-th node from the end of list 
// and return its head.

// Example:

// Given linked list: 1->2->3->4->5, and n = 2.

// After removing the second node from the end, the linked list
//  becomes 1->2->3->5.

// Note:

// Given n will always be valid.

// Follow up:

// Could you do this in one pass?
