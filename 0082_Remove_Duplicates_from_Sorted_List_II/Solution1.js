import { ListNode, ListUtils } from './utils_js/list.js';



/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
  let dummyHead = new ListNode(0);
  dummyHead.next = head;
  let newTail = dummyHead;
  let p = dummyHead.next;

  while (p && p.next) {

    if (p.val == p.next.val) {
      while (p.next && p.val == p.next.val) {
        p = p.next;
      }
      newTail.next = p.next;
      p = p.next;
      continue;
    }
    newTail = newTail.next;
    p = p.next;
  }
  return dummyHead.next;
};

function test(testName, head, expected) {
  let res = deleteDuplicates(head);
  if (ListUtils.isEqualList(res, expected))
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}

let head1 = ListUtils.buildList([1,2,3,3,4,4,5]);
let expected1 = ListUtils.buildList([1,2,5]);
test('test1', head1, expected1);

let head2 = ListUtils.buildList([1,1,1,2,3]);
let expected2 = ListUtils.buildList([2,3]);
test('test2', head2, expected2);


// Given a sorted linked list, delete all nodes that have duplicate numbers,
// leaving only distinct numbers from the original list.

// Return the linked list sorted as well.

// Example 1:

// Input: 1->2->3->3->4->4->5
// Output: 1->2->5
// Example 2:

// Input: 1->1->1->2->3
// Output: 2->3

