/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
  if (prerequisites.length === 0)
    return true;

  let inDegrees = Array(numCourses).fill(0);
  let adjs = Array(numCourses);
  for (let i = 0; i < numCourses; i++) {
    adjs[i] = new Set();
  }

  for (let i = 0; i < prerequisites.length; i++) {
    let end = prerequisites[i][0];
    let start = prerequisites[i][1];
    inDegrees[end]++;
    adjs[start].add(end);
  }

  let que = [];
  for (let i = 0; i < inDegrees.length; i++) {
    if (inDegrees[i] === 0) {
      que.push(i);
    }
  }

  let cnt = 0;   // 已经学习过的课程的数量
  while (que.length) {
    let curNode = que.shift();
    cnt++;

    for (let successor of adjs[curNode]) {
      if (--inDegrees[successor] === 0) {
        que.push(successor);
      }
    }
  }

  return cnt === numCourses;
};

function test(testName, numCourses, prerequisites, expected) {
  let res = canFinish(numCourses, prerequisites);
  if (res == expected)
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}

let numCourses1 = 2;
let prerequisites1 = [[1,0]];
let expected1 = true;
test('test1', numCourses1, prerequisites1, expected1);

let numCourses2 = 2;
let prerequisites2 = [[1,0],[0,1]];
let expected2 = false;
test('test2', numCourses2, prerequisites2, expected2);

let numCourses3 = 3;
let prerequisites3 = [[1,0], [1,2], [0,1]];
let expected3 = false;
test('test3', numCourses3, prerequisites3, expected3);


// There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

// Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
// which is expressed as a pair: [0,1]

// Given the total number of courses and a list of prerequisite pairs,
// is it possible for you to finish all courses?

//  

// Example 1:

// Input: numCourses = 2, prerequisites = [[1,0]]
// Output: true
// Explanation: There are a total of 2 courses to take.
//              To take course 1 you should have finished course 0. So it is possible.
// Example 2:

// Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
// Output: false
// Explanation: There are a total of 2 courses to take.
//              To take course 1 you should have finished course 0, and to take course 0 you should
//              also have finished course 1. So it is impossible.
//  

// Constraints:

// The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
// You may assume that there are no duplicate edges in the input prerequisites.
// 1 <= numCourses <= 10^5