/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var findNumberIn2DArray = function(matrix, target) {
  if (!matrix.length) return false;
  if (!matrix[0].length) return false;
  let m = matrix.length, n = matrix[0].length;

  let x = 0, y = n - 1;
  while (x < m && 0 <= y) {
    if (matrix[x][y] == target) return true;
    else if (target < matrix[x][y]) y--;
    else x++;
  }

  return false;
};

function test(testName, matrix, target, expected) {
  let res = findNumberIn2DArray(matrix, target);
  if (res == expected)
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}

let matrix1 = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
];
let target1 = 5;
let expected1 = true;
test('test1', matrix1, target1, expected1);

let matrix2 = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
];
let target2 = 20;
let expected2 = false;
test('test2', matrix2, target2, expected2);
