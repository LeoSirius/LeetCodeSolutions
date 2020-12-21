import { is_equal_array } from './utils_js/array.js';

/**
 * Initialize your data structure here.
 */
var MyQueue = function() {
  this.istk = [];
  this.ostk = []
};

/**
 * Push element x to the back of queue. 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
  this.istk.push(x);
};

/**
 * Removes the element from in front of queue and returns that element.
 * @return {number}
 */
MyQueue.prototype.pop = function() {
  if (this.ostk.length == 0) {
    let istk_length = this.istk.length;
    while (istk_length--) {
      this.ostk.push(this.istk.pop());
    }
  }
  return this.ostk.pop();
};

/**
 * Get the front element.
 * @return {number}
 */
MyQueue.prototype.peek = function() {
  if (this.ostk.length == 0) {
    let istk_length = this.istk.length;
    while (istk_length--) {
      this.ostk.push(this.istk.pop());
    }
  }
  return this.ostk[this.ostk.length-1];
};

/**
 * Returns whether the queue is empty.
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
  return this.istk.length == 0 && this.ostk.length == 0;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */

function test1() {
  let obj = new MyQueue();
  obj.push(1);
  obj.push(2);
  let res1 = obj.peek();    // 1
  let res2 = obj.pop();     // 1
  let res3 = obj.empty();   // false

  if (is_equal_array([res1, res2, res3], [1, 1, false])) {
    console.log('test1 success.');
  } else {
    console.log('test1 failed.');
  }
}

test1();


// Implement the following operations of a queue using stacks.

// push(x) -- Push element x to the back of queue.
// pop() -- Removes the element from in front of queue.
// peek() -- Get the front element.
// empty() -- Return whether the queue is empty.
// Example:

// MyQueue queue = new MyQueue();

// queue.push(1);
// queue.push(2);  
// queue.peek();  // returns 1
// queue.pop();   // returns 1
// queue.empty(); // returns false
// Notes:

// You must use only standard operations of a stack --
// which means only push to top, peek/pop from top, size, 
// and is empty operations are valid.
// Depending on your language, stack may not be supported natively.
// You may simulate a stack by using a list or deque (double-ended queue),
// as long as you use only standard operations of a stack.
// You may assume that all operations are valid (for example,
// no pop or peek operations will be called on an empty queue).