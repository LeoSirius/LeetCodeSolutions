import { ListNode, is_equal_list } from './utils_js/list.js';

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
  let dummy = new ListNode();
  let p = dummy;
  while (l1 || l2) {
    let v1 = l1 ? l1.val : Number.MAX_SAFE_INTEGER;
    let v2 = l2 ? l2.val : Number.MAX_SAFE_INTEGER;
    if (v1 < v2) {
      p.next = l1;
      l1 = l1.next;
    } else {
      p.next = l2;
      l2 = l2.next;
    }
    p = p.next;
  }
  return dummy.next;
};

function test(test_name, l1, l2, expected) {
  let res = mergeTwoLists(l1, l2);
  if (is_equal_list(res, expected)) {
    console.log(test_name + ' sucess.');
  } else {
    console.log(test_name + ' failed.');
  }
}

let l11 = new ListNode(1);
l11.next = new ListNode(2);
l11.next.next = new ListNode(4);

let l21 = new ListNode(1);
l21.next = new ListNode(3);
l21.next.next = new ListNode(4);

let expected1 = new ListNode(1);
expected1.next = new ListNode(1);
expected1.next.next = new ListNode(2);
expected1.next.next.next = new ListNode(3);
expected1.next.next.next.next = new ListNode(4);
expected1.next.next.next.next.next = new ListNode(4);

// 输入：1->2->4, 1->3->4
// 输出：1->1->2->3->4->4
test("test1", l11, l21, expected1);

// 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

// 示例1：
// 输入：1->2->4, 1->3->4
// 输出：1->1->2->3->4->4

// 限制：
// 0 <= 链表长度 <= 1000
