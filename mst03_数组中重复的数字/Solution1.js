/**
 * @param {number[]} nums
 * @return {number}
 */
var findRepeatNumber = function(nums) {
  for (let i = 0; i < nums.length; i++) {
    while (nums[i] != i) {
      if (nums[nums[i]] === nums[i]) return nums[i];
      let tmp = nums[nums[i]];
      nums[nums[i]] = nums[i];
      nums[i] = tmp;
    }
  }
};

function test(testName, nums, expectedArr) {
  let res = findRepeatNumber(nums);
  if (expectedArr.indexOf(res) !== -1)
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}

let nums1 = [2,3,1,0,2,5,3];
let expectedArr1 = [2,3];
test('test1', nums1, expectedArr1);


    // vector<int> nums1 = {2, 3, 1, 0, 2, 5, 3};
    // vector<int> expected1 = {2,3};
    // test("test1", nums1, expected1)

// [2, 3, 1, 0, 2, 5, 3]
// 输出：2 或 3 

// 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
// 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
// 请找出数组中任意一个重复的数字。

// 限制：

// 2 <= n <= 100000