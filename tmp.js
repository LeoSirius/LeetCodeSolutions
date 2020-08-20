/**
 * Initialize your data structure here.
 */
var TwoSum = function() {
  this.hashmap = {};
};

/**
 * Add the number to an internal data structure.. 
 * @param {number} number
 * @return {void}
 */
TwoSum.prototype.add = function(number) {
  if (number in this.hashmap) 
};

/**
 * Find if there exists any pair of numbers which sum is equal to the value. 
 * @param {number} value
 * @return {boolean}
 */
TwoSum.prototype.find = function(value) {

};

/**
 * Your TwoSum object will be instantiated and called as such:
 * var obj = new TwoSum()
 * obj.add(number)
 * var param_2 = obj.find(value)
 */

// Design and implement a TwoSum class. It should support the following operations: add and find.

// add - Add the number to an internal data structure.
// find - Find if there exists any pair of numbers which sum is equal to the value.

// Example 1:

// add(1); add(3); add(5);
// find(4) -> true
// find(7) -> false
// Example 2:

// add(3); add(1); add(2);
// find(3) -> true
// find(6) -> false
