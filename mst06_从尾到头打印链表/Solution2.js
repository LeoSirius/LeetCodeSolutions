import { ListNode, ListUtils } from './utils_js/list.js';
import { ArrayUtils } from './utils_js/array.js';

/**
 * @param {ListNode} head
 * @return {number[]}
 */
var reversePrint = function(head) {
  let resArr = [];
  if (!head || head.length === 0) return resArr;

  let postOrder = (node) => {
    if (node.next) postOrder(node.next);
    resArr.push(node.val);
  }
  postOrder(head);
  return resArr;
};

function test(testName, head, expected) {
  let res = reversePrint(head);
  console.log('res = ', res)
  if (ArrayUtils.isEqualArray(res, expected))
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}

let l1 = ListUtils.buildList([1,3,2]);
let expected1 = [2,3,1];
test('test1', l1, expected1);

let l2 = ListUtils.buildList([]);
let expected2 = [];
test('test2', l2, expected2);
