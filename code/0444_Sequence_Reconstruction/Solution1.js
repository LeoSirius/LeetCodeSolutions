/**
 * @param {number[]} org
 * @param {number[][]} seqs
 * @return {boolean}
 */
var sequenceReconstruction = function(org, seqs) {
  if (!seqs.length)
    return false;
  if (seqs.every(seq => seq.length === 0))
    return false;

  let size = org.length;
  let graph = [];
  let indegrees = Array(size+1).fill(0);

  // build graph and indegrees
  for (let seq of seqs) {
    // seqs中有在size范围之外的数，直接false
    if (seq.some(n => n < 1 || size < n)) return false;

    for (let i = 1; i < seq.length; i++) {
      if (!graph.hasOwnProperty(seq[i-1])) graph[seq[i-1]] = [];
      if (graph[seq[i-1]].indexOf(seq[i]) === -1) {
        graph[seq[i-1]].push(seq[i])
        indegrees[seq[i]]++;
      }
    }
  }

  let layer = org.filter(item => indegrees[item] === 0);
  for (let i = 0; i < size; i++) {
    if (layer.length > 1 || layer[0] !== org[i]) return false;

    let nextLayer = [];
    if (!graph[layer[0]]) continue;
    for (let adjNode of graph[layer[0]]) {
      if ((--indegrees[adjNode]) === 0) {
        nextLayer.push(adjNode);
      }
    }
    layer = nextLayer;
  }

  return true;
};

function test(testName, org, seqs, expected) {
  let res = sequenceReconstruction(org, seqs);
  if (res == expected)
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}


let org1 = [1,2,3];
let seqs1 = [[1,2],[1,3]];
let expected1 = false;
test('test1', org1, seqs1, expected1);

let org2 = [1,2,3];
let seqs2 = [[1,2]];
let expected2 = false;
test('test2', org2, seqs2, expected2);

let org3 = [1,2,3];
let seqs3 = [[1,2],[1,3],[2,3]];
let expected3 = true;
test('test3', org3, seqs3, expected3);

let org4 = [4,1,5,2,6,3];
let seqs4 = [[5,2,6,3],[4,1,5,2]];
let expected4 = true;
test('test4', org4, seqs4, expected4);

let org5 = [1];
let seqs5 = [[],[]];
let expexted5 = false;
test('test5', org5, seqs5, expexted5);

let org6 = [3,7,6,4,8,2,10,1,5,9];
let seqs6 = [[7,6,4,8,2,10,1,5,9],[4,8,2,10,1,5],[2,10,1,5],[10,1,5,9],[1,5,9],[8,2,10,1,5,9],[9],[],[6,4],[3,7,6,4,8,2,10,1]];
let expected6 = true;
test('test6', org6, seqs6, expected6);


// Check whether the original sequence org can be uniquely reconstructed from 
// the sequences in seqs. 
// The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104.
//  Reconstruction means building a shortest common supersequence of the
//   sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are
//    subsequences of it). Determine whether there is only one sequence that can be 
//    reconstructed from seqs and it is the org sequence.

// Example 1:
// Input: org = [1,2,3], seqs = [[1,2],[1,3]]
// Output: false
// Explanation: [1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

// Example 2:
// Input: org = [1,2,3], seqs = [[1,2]]
// Output: false
// Explanation: The reconstructed sequence can only be [1,2].

// Example 3:
// Input: org = [1,2,3], seqs = [[1,2],[1,3],[2,3]]
// Output: true
// Explanation: The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

// Example 4:
// Input: org = [4,1,5,2,6,3], seqs = [[5,2,6,3],[4,1,5,2]]
// Output: true

// Constraints:
// 1 <= n <= 10^4
// org is a permutation of {1,2,...,n}.
// seqs[i][j] fits in a 32-bit signed integer.