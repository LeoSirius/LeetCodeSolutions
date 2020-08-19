/**
 * initialize your data structure here.
 */
var MinStack = function() {
  this.stk = [];
  this.min_stk = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
  this.stk.push(x);
  if (this.min_stk.length === 0 || x <= this.min_stk[this.min_stk.length-1]) {
    this.min_stk.push(x);
  }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
  var res = this.stk.pop();
  if (this.min_stk.length > 0 && this.min_stk[this.min_stk.length-1] === res) {
    this.min_stk.pop();
  }
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
  return this.stk[this.stk.length-1];
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
  return this.min_stk[this.min_stk.length-1];
};

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(x)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */

function test1() {
  var obj = new MinStack();
  obj.push(-2);
  obj.push(0);
  obj.push(-3);
  var res1 = obj.getMin();   // -3
  obj.pop();
  var res2 = obj.top();      // 0
  var res3 = obj.getMin();   // -2
  if (JSON.stringify([res1, res2, res3]) === JSON.stringify([-3, 0, -2])) {
    console.log('test1 success.');
  } else {
    console.log('test1 failed.');
  }
}

test1();





// 定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，
// 调用 min、push 及 pop 的时间复杂度都是 O(1)。

// 示例:
// MinStack minStack = new MinStack();
// minStack.push(-2);
// minStack.push(0);
// minStack.push(-3);
// minStack.min();   --> 返回 -3.
// minStack.pop();
// minStack.top();      --> 返回 0.
// minStack.min();   --> 返回 -2.
//  

// 提示：

// 各函数的调用总次数不超过 20000 次
//  

// 注意：本题与主站 155 题相同