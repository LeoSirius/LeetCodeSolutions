import { ListNode, is_equal_list } from './utils_js/list.js';


/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  let p1 = l1, p2 = l2;
  let carry = 0;
  let res_head = new ListNode(0);
  let res_p = res_head;
  while (p1 || p2 || carry) {
    let v1 = p1 ? p1.val : 0;
    let v2 = p2 ? p2.val : 0;
    let sum = v1 + v2 + carry;
    res_p.next = new ListNode(sum % 10);
    res_p = res_p.next;
    carry = Math.floor(sum / 10);
    p1 = p1 ? p1.next : p1;
    p2 = p2 ? p2.next : p2;
  }
  return res_head.next;
};

function test(test_name, l1, l2, expected) {
  let res = addTwoNumbers(l1, l2);
  if (is_equal_list(res, expected))
    console.log(test_name + ' success.');
  else
    console.log(test_name + ' failed.');
}

let a1 = new ListNode(2);
a1.next = new ListNode(4);
a1.next.next = new ListNode(3);

let b1 = new ListNode(5);
b1.next = new ListNode(6);
b1.next.next = new ListNode(4);

let c1 = new ListNode(7);
c1.next = new ListNode(0);
c1.next.next = new ListNode(8);

// 2->4->3 + 5->6->4 = 7->0->8
test("test1", a1, b1, c1);


let a2 = new ListNode(5);
let b2 = new ListNode(5);
let c2 = new ListNode(0);
c2.next = new ListNode(1);

test('test2', a2, b2, c2);