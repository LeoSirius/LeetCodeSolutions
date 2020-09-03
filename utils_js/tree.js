function TreeNode(val, left, right) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
}

function getInOrderArray(tree) {
  let resArr = [];
  let stk = [];
  let p = tree;
  while (p || stk.length) {
    while (p) {
      stk.push(p);
      p = p.left;
    }
    p = stk.pop();
    resArr.push(p.val);
    p = p.right;
  }
  return resArr;
}

const TreeUtils = {
  getInOrderArray: getInOrderArray,
};

export { TreeUtils, TreeNode };