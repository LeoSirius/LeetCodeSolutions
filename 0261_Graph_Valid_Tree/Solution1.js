/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {boolean}
 */
var validTree = function(n, edges) {

  // 这是无向图，且edges的元素是unique的
  // 如果边数 >= 顶点数，则必然存在环，可以直接pass
  if (edges.length >= n)
    return false;

  let graph = {};   // key is node number, value is adj list

  // build graph
  for (let i = 0; i < edges.length; i++) {
    let x = edges[i][0], y = edges[i][1];
    if (!graph.hasOwnProperty(x))
      graph[x] = [];
    if (!graph.hasOwnProperty(y))
      graph[y] = [];
    graph[x].push(y);
    graph[y].push(x);
  }

  let visitedSet = new Set();
  let edgesUsed = 0;

  let dfs = function(nodeNum) {
    visitedSet.add(nodeNum);
    if (!graph.hasOwnProperty(nodeNum))
      return;
    for (let adjNode of graph[nodeNum]) {
      if (visitedSet.has(adjNode))
        continue;
      dfs(adjNode);
      edgesUsed++;    // 每调用一次dfs，即是走过了一条边
    }
  }

  dfs(0);

  return visitedSet.size === n;
};

function test(testName, n, edges, expected) {
  let res  =validTree(n, edges);
  console.log(res)
  if (res == expected)
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}

let n1 = 5;
let edges1 = [[0,1], [0,2], [0,3], [1,4]];
let expected1 = true;
test('test1', n1, edges1, expected1);

let n2 = 5;
let edges2 = [[0,1], [1,2], [2,3], [1,3], [1,4]];
let expected2 = false;
test('test2', n2, edges2, expected2);

let n3 = 4;
let edges3 = [[2,3],[1,2],[1,3]];
let expected3 = false;
test('test3', n3, edges3, expected3);

let n4 = 4;
let edges4 = [[0,1],[2,3],[1,2]];
let expected4 = true;
test('test4', n4, edges4, expected4);


// Given n nodes labeled from 0 to n-1 and a list of undirected edges
//  (each edge is a pair of nodes), write a function to check whether 
//  these edges make up a valid tree.

// Example 1:

// Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
// Output: true

// Example 2:
// Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
// Output: false

// Note: you can assume that no duplicate edges will appear in edges.
//  Since all edges are undirected, [0,1] is the same as [1,0] and thus
//   will not appear together in edges.

