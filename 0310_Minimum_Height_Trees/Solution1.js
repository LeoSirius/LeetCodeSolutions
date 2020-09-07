import { ArrayUtils } from './utils_js/array.js';

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findMinHeightTrees = function(n, edges) {
  if (n == 1) return [0];

  let graph = {};
  let degrees = new Array(n).fill(0);
  for (let i = 0; i < edges.length; i++) {
    let x = edges[i][0], y = edges[i][1];
    if (!graph.hasOwnProperty(x)) graph[x] = [];
    if (!graph.hasOwnProperty(y)) graph[y] = [];
    graph[x].push(y);
    graph[y].push(x);
    degrees[x]++;
    degrees[y]++;
  }

  let layer = [];
  for (let i = 0; i < degrees.length; i++) {
    if (degrees[i] == 1) layer.push(i);
  }

  while (layer.length) {
    let nextLayer = [];
    for (let leaf of layer) {
      for (let neighborOfLeaf of graph[leaf]) {
        degrees[neighborOfLeaf]--;
        if (degrees[neighborOfLeaf] == 1) nextLayer.push(neighborOfLeaf);
      }
    }
    if (nextLayer.length === 0) return layer;
    layer = nextLayer;
  }
};

function test(testName, n, edges, expected) {
  let res = findMinHeightTrees(n, edges);
  if (ArrayUtils.isEqualArray(res, expected))
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}



let n1 = 4;
let edges1 = [[1, 0], [1, 2], [1, 3]];
let expected1 = [1];
//          0
//          |
//          1
//         / \
//        2   3 
test('test1', n1, edges1, expected1);

let n2 = 6;
let edges2 = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]];
let expected2 = [3, 4];
//       0  1  2
//        \ | /
//          3
//          |
//          4
//          |
//          5 
test('test2', n2, edges2, expected2);



// For an undirected graph with tree characteristics, we can choose any node as the root.
//  The result graph is then a rooted tree. Among all possible rooted trees, those 
//  with minimum height are called minimum height trees (MHTs). Given such a graph,
//   write a function to find all the MHTs and return a list of their root labels.

// Format
// The graph contains n nodes which are labeled from 0 to n - 1. You will 
// be given the number n and a list of undirected edges (each edge is a pair of labels).

// You can assume that no duplicate edges will appear in edges. Since all 
// edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear 
// together in edges.

// Example 1 :
// Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

//         0
//         |
//         1
//        / \
//       2   3 

// Output: [1]

// Example 2 :
// Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

//      0  1  2
//       \ | /
//         3
//         |
//         4
//         |
//         5 

// Output: [3, 4]

// Note:

// According to the definition of tree on Wikipedia: “
// a tree is an undirected graph in which any two vertices are connected 
// by exactly one path. In other words, any connected graph without simple
//  cycles is a tree.”
// The height of a rooted tree is the number of edges on the longest
//  downward path between the root and a leaf.
