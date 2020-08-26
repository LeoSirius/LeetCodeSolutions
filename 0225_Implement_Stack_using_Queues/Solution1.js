import { is_equal_array } from './utils_js/array.js';
// let is_equal_array

/**
 * Initialize your data structure here.
 */
var MyStack = function() {
  this.que = [];
};

/**
 * Push element x onto stack. 
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
  let old_length = this.que.length;
  this.que.push(x);
  while (old_length--) {
    let item = this.que.shift();

    this.que.push(item);
  }
};

/**
 * Removes the element on top of the stack and returns that element.
 * @return {number}
 */
MyStack.prototype.pop = function() {
  return this.que.shift();
};

/**
 * Get the top element.
 * @return {number}
 */
MyStack.prototype.top = function() {
  return this.que[0];
};

/**
 * Returns whether the stack is empty.
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
  return this.que.length == 0;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * var obj = new MyStack()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.empty()
 */

function test1() {
  let obj = new MyStack();
  obj.push(1);
  obj.push(2);
  let res1 = obj.top();     // 2
  let res2 = obj.pop();     // 2
  let res3 = obj.empty();   // false
  console.log('[res1, res2, res3] = ', [res1, res2, res3])
  if (is_equal_array([res1, res2, res3], [2, 2, false])) {
    console.log('test1 success.');
  } else {
    console.log('test1 failed.');
  }
}

test1();

// Implement the following operations of a stack using queues.

// push(x) -- Push element x onto stack.
// pop() -- Removes the element on top of the stack.
// top() -- Get the top element.
// empty() -- Return whether the stack is empty.
// Example:

// MyStack stack = new MyStack();

// stack.push(1);
// stack.push(2);  
// stack.top();   // returns 2
// stack.pop();   // returns 2
// stack.empty(); // returns false
// Notes:

// You must use only standard operations of a queue -- 
// which means only push to back, peek/pop from front, size, 
// and is empty operations are valid.

// Depending on your language, queue may not be supported natively.
// You may simulate a queue by using a list or deque (double-ended queue),
// as long as you use only standard operations of a queue.

// You may assume that all operations are valid (for example, 
// no pop or top operations will be called on an empty stack).