/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
  
};

function test(testName, nums, k, expected) {
  let res = findKthLargest(nums, k);
  if (res == expected)
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}


let nums1 = [3,2,1,5,6,4]
let k1 = 2
let expected1 = 5
test('test1', nums1, k1, expected1)

let nums2 = [3,2,3,1,2,4,5,5,6]
let k2 = 4
let expected2 = 4
test('test2', nums2, k2, expected2)


// Find the kth largest element in an unsorted array. 
// Note that it is the kth largest element in the sorted order, 
// not the kth distinct element.

// Example 1:
// Input: [3,2,1,5,6,4] and k = 2
// Output: 5

// Example 2:
// Input: [3,2,3,1,2,4,5,5,6] and k = 4
// Output: 4
// Note:
// You may assume k is always valid, 1 ≤ k ≤ array's length.