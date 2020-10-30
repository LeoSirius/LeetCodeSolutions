import { is_equal_array } from './utils_js/array.js';

/**
 * @param {number[][]} v
 */
var Vector2D = function(v) {
  this.flated = [];
  this.idx = 0;
  for (let row of v) {
    this.flated = this.flated.concat(row);
  }
};

/**
 * @return {number}
 */
Vector2D.prototype.next = function() {
  return this.flated[this.idx++];
};

/**
 * @return {boolean}
 */
Vector2D.prototype.hasNext = function() {
  return this.idx < this.flated.length;
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * var obj = new Vector2D(v)
 * var param_1 = obj.next()
 * var param_2 = obj.hasNext()
 */

function test1() {
  let v = [[1,2],[3],[4]];
  let obj = new Vector2D(v);

  let res1 = obj.next();     // 1
  let res2 = obj.next();     // 2
  let res3 = obj.next();     // 3
  let res4 = obj.hasNext();  // true
  let res5 = obj.hasNext();  // true
  let res6 = obj.next();     // 4
  let res7 = obj.hasNext();  // false
  if (is_equal_array([res1, res2, res3, res4, res5, res6, res7],
    [1, 2, 3, true, true, 4, false]
  )) {
    console.log('test1 success.');
  } else {
    console.log('test1 failed.');
  }
}

test1();


// Design and implement an iterator to flatten a 2d vector. 
// It should support the following operations: next and hasNext.

//  

// Example:

// Vector2D iterator = new Vector2D([[1,2],[3],[4]]);

// iterator.next(); // return 1
// iterator.next(); // return 2
// iterator.next(); // return 3
// iterator.hasNext(); // return true
// iterator.hasNext(); // return true
// iterator.next(); // return 4
// iterator.hasNext(); // return false
//  

// Notes:

// Please remember to RESET your class variables declared in Vector2D,
// as static/class variables are persisted across multiple test cases. 
// Please see here for more details.
// You may assume that next() call will always be valid, that is, 
// there will be at least a next element in the 2d vector when next() is called.

