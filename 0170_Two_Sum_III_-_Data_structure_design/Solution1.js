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
  if (!(number in this.hashmap)) {
    this.hashmap[number] = 1;
    // console.log('afteradd,1 this.hashmap = ', this.hashmap)
    return;
  }
  this.hashmap[number]++;
  // console.log('afteradd,2 this.hashmap = ', this.hashmap)
};

/**
 * Find if there exists any pair of numbers which sum is equal to the value. 
 * @param {number} value
 * @return {boolean}
 */
TwoSum.prototype.find = function(value) {
  for (let key in this.hashmap) {
    let num2found = value - key;
    // 如果是 3 + 3 == 6这种，3必须出现大于1次
    if (num2found == key && this.hashmap[num2found] > 1) 
      return true;
    // 如果不是两个相同的数，就不用管次数
    if (num2found != key && this.hashmap.hasOwnProperty(num2found)) {
      return true;
    }
  }
  return false;
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

// 临时加入用来比较数组
// Warn if overriding existing method
if(Array.prototype.equals)
    console.warn("Overriding existing Array.prototype.equals. Possible causes: New API defines the method, there's a framework conflict or you've got double inclusions in your code.");
// attach the .equals method to Array's prototype to call it on any array
Array.prototype.equals = function (array) {
    // if the other array is a falsy value, return
    if (!array)
        return false;

    // compare lengths - can save a lot of time
    if (this.length != array.length)
        return false;

    for (var i = 0, l=this.length; i < l; i++) {
        // Check if we have nested arrays
        if (this[i] instanceof Array && array[i] instanceof Array) {
            // recurse into the nested arrays
            if (!this[i].equals(array[i]))
                return false;       
        }           
        else if (this[i] != array[i]) { 
            // Warning - two different object instances will never be equal: {x:20} != {x:20}
            return false;   
        }           
    }       
    return true;
}
// Hide method from for-in loops
Object.defineProperty(Array.prototype, "equals", {enumerable: false});

function test1() {
  var obj = new TwoSum();
  obj.add(1); obj.add(3); obj.add(5);
  let res1 = obj.find(4);    // true
  let res2 = obj.find(7);    // false
  if ([res1, res2].equals([true, false])) {
    console.log('test1 success.');
  } else {
    console.log('test1 failed.')
  }
}

function test2() {
  var obj = new TwoSum();
  obj.add(3); obj.add(1); obj.add(2);
  let res1 = obj.find(3);    // true
  let res2 = obj.find(6);    // false
  if ([res1, res2].equals([true, false])) {
    console.log('test2 success.');
  } else {
    console.log('test2 failed.')
  }
}

function test3() {
  var obj = new TwoSum();
  obj.add(0); obj.add(0);
  let res1 = obj.find(0);
  if (res1 == true) {
    console.log('test3 success.');
  } else {
    console.log('test3 failed.')
  }
}

test1();
test2();
test3();

// Example 1:

// add(1); add(3); add(5);
// find(4) -> true
// find(7) -> false

// Example 2:

// add(3); add(1); add(2);
// find(3) -> true
// find(6) -> false
