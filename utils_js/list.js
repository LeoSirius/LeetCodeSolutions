function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val);
    this.next = (next===undefined ? null : next);
}

function is_equal_list(l1, l2) {
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

export { ListNode, is_equal_list };