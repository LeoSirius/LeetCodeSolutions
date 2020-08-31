
function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val);
  this.next = (next===undefined ? null : next);
}

function isEqualList(l1, l2) {
  let p1 = l1;
  let p2 = l2;
  while (p1 && p2) {
    if (p1.val != p2.val)
      return false;
    p1 = p1.next;
    p2 = p2.next;
  }
  if (p1 || p2)
    return false;
  return true;
}

function printList(list) {
  let p = list;
  while (p) {
    console.log(p.val);
    p = p.next;
  }
}

const ListUtils = {
  isEqualList: isEqualList,
  printList: printList,
};

export { ListUtils, ListNode };