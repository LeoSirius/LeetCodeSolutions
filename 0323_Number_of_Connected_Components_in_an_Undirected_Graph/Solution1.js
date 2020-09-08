/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countComponents = function(n, edges) {
  let parents = Array.from(Array(n).keys());

  // find 的作用是找到x的根结点
  let find = (x) => {
    if (x === parents[x]) return x;
    return find(parents[x]);
  }

  // union 的作用是把x所在的连通分量和y所在的连通分量合并
  let union = (x, y) => {
    parents[find(x)] = parents[find(y)];   // 这里是把x的根放到了y的根的下面
  }

  for (let i = 0; i < edges.length; i++) {
    union(edges[i][0], edges[i][1]);   // 每一个edge的两个点本身是连通的，所以把它们合并在一起
  }

  let rootCount = 0;
  for (let i = 0; i < parents.length; i++)
    if (parents[i] === i) rootCount++;
  
  return rootCount;
};

function test(testName, n, edges, expected) {
  let res = countComponents(n, edges);
  if (res == expected)
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}


let n1 = 5;
let edges1 = [[0, 1], [1, 2], [3, 4]];
let expected1 = 2;
//       0          3
//       |          |
//       1 --- 2    4 
test('test1', n1, edges1, expected1);


let n2 = 5;
let edges2 = [[0, 1], [1, 2], [2, 3], [3, 4]];
//       0           4
//       |           |
//       1 --- 2 --- 3
let expected2 = 1;
test('test2', n2, edges2, expected2);



// Given n nodes labeled from 0 to n - 1 and a list of undirected 
// edges (each edge is a pair of nodes), write a function to find the
//  number of connected components in an undirected graph.

// Example 1:

// Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

//      0          3
//      |          |
//      1 --- 2    4 

// Output: 2
// Example 2:

// Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

//      0           4
//      |           |
//      1 --- 2 --- 3

// Output:  1
// Note:
// You can assume that no duplicate edges will appear in edges. 
// Since all edges are undirected, [0, 1] is the same as [1, 0] and 
// thus will not appear together in edges.

