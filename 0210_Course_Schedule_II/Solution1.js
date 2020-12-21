import { ArrayUtils } from './utils_js/array.js';

/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {number[]}
 */
var findOrder = function(numCourses, prerequisites) {
  if (numCourses === 1)
    return [0];
  
  let inDegrees = Array(numCourses).fill(0);
  let adjs = Array(numCourses);
  for (let i = 0; i < numCourses; i++)
    adjs[i] = new Set();

  for (let i = 0; i < prerequisites.length; i++) {
    let end = prerequisites[i][0];
    let start = prerequisites[i][1];
    inDegrees[end]++;
    adjs[start].add(end);
  }

  let que = [];
  for (let i = 0; i < numCourses; i++) {
    if (inDegrees[i] == 0) {
      que.push(i);
    }
  }

  let path = [];
  let cnt = 0;
  while (que.length) {
    let curNode = que.shift();
    path.push(curNode);
    cnt++;

    for (let successor of adjs[curNode]) {
      if (--inDegrees[successor] === 0) {
        que.push(successor);
      }
    }
  }

  return cnt == numCourses ? path : [];
};

function test(testName, numCourses, prerequisite, expectedArr) {
  let res = findOrder(numCourses, prerequisite);
  if (expectedArr.find(arr => ArrayUtils.isEqualArray(arr, res)))
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}

let numCourses1 = 2;
let prerequisites1 = [[1,0]];
let expectedArr1 = [[0,1]];
test('test1', numCourses1, prerequisites1, expectedArr1);

let numCourses2 = 4;
let prerequisites2 = [[1,0],[2,0],[3,1],[3,2]];
let expectedArr2 = [[0,1,2,3], [0,2,1,3]];
test('test2', numCourses2, prerequisites2, expectedArr2);

let numCourses3 = 1;
let prerequisites3 = [];
let expectedArr3 = [[0]];
test('test3', numCourses3, prerequisites3, expectedArr3);


// There are a total of n courses you have to take, labeled from 0 to n-1.

// Some courses may have prerequisites, for example to take course 0
// you have to first take course 1, which is expressed as a pair: [0,1]

// Given the total number of courses and a list of prerequisite pairs,
// return the ordering of courses you should take to finish all courses.

// There may be multiple correct orders, you just need to return one of them.
// If it is impossible to finish all courses, return an empty array.


// Input: 2, [[1,0]]
// Output: [0,1]
// Explanation: There are a total of 2 courses to take. To take course 1 you should have finished
//              course 0. So the correct course order is [0,1] .
// Example 2:

// Input: 4, [[1,0],[2,0],[3,1],[3,2]]
// Output: [0,1,2,3] or [0,2,1,3]
// Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both
//              courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
//              So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .


// Constraints:

// 1 <= numCourses <= 2000
// 0 <= prerequisites.length <= numCourses * (numCourses - 1)
// prerequisites[i].length == 2
// 0 <= ai, bi < numCourses
// ai != bi
// All the pairs [ai, bi] are distinct.

