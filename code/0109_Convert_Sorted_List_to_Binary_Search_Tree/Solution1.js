import { ListNode, ListUtils } from './utils_js/list.js';
import { TreeNode, TreeUtils } from './utils_js/tree.js';


function buildTree(head, tail) {
  if (head == tail)
    return null;      // 这里必须是null， 不能是undefined 或其他类型
  let fast = head, slow = head;
  while (fast != tail && fast.next != tail) {
    fast = fast.next.next;
    slow = slow.next;
  }
  let centerNode = new TreeNode(slow.val);
  centerNode.left = buildTree(head, slow);
  centerNode.right = buildTree(slow.next, tail);
  return centerNode;
}

/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function(head) {
  // 左闭右开
  return buildTree(head, null);
};


function test(testName, head, expectedArr) {
  let res = sortedListToBST(head);
  // 这道题不要用is_equal_tree来测试，答案不唯一。但是他们的中序遍历的结果一定是唯一的
  let inOrderArr = TreeUtils.getInOrderArray(res);
  if (ListUtils.isEqualList(inOrderArr, expectedArr))
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}


//     test('test1', head1, expected_arr1)

let head1 = ListUtils.buildList([-10, -3, 0, 5, 9]);
let expectedArr1 = [-10,-3,0,5,9];
//     #       0
//     #      / \
//     #    -3   9
//     #    /   /
//     #  -10  5
test('test1', head1, expectedArr1);



// Given a singly linked list where elements are sorted in ascending order,
// convert it to a height balanced BST.

// For this problem, a height-balanced binary tree is defined as a binary
// tree in which the depth of the two subtrees of every node never differ by more than 1.
