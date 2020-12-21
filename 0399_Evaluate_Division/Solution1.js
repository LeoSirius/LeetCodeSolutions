import { ArrayUtils } from './utils_js/array.js';

/**
 * @param {string[][]} equations
 * @param {number[]} values
 * @param {string[][]} queries
 * @return {number[]}
 */
var calcEquation = function(equations, values, queries) {
  let graph = {};
  let weight = {};

  // build graph
  for (let i = 0; i < equations.length; i++) {
    let start = equations[i][0], end = equations[i][1];

    if (!graph.hasOwnProperty(start)) graph[start] = [];
    if (!graph.hasOwnProperty(end)) graph[end] = [];

    graph[start].push(end);
    graph[end].push(start);
    weight[[start, end]] = values[i];
    weight[[end, start]] = 1 / values[i];
  }

  let visited = new Set();

  let dfs = function(start, end) {
    if (weight.hasOwnProperty([start, end]))
      return weight[[start, end]];

    if (!graph.hasOwnProperty(start) || !graph.hasOwnProperty(end))
      return 0.0;
    if (visited.has(start))   // 已经访问过的必须跳出，不然是调用的死循环
      return 0.0;

    visited.add(start);
    let res = 0;
    for (let adjNode of graph[start]) {
      res = weight[[start, adjNode]] * dfs(adjNode, end);
      if (res !== 0.0) {
        weight[[start, end]] = res;
        break;    // 只需要找到一条路径，即可break掉
      }
    }
    visited.delete(start);
    return res;
  }

  let res = [];
  for (let i = 0; i < queries.length; i++) {
    let start = queries[i][0], end = queries[i][1];
    let tmpRes = dfs(start, end);
    if (tmpRes === 0.0) tmpRes = -1.0;
    res.push(tmpRes);
  }
  return res;
};

function test(testName, equations, values, queries, expected) {
  let res = calcEquation(equations, values, queries);
  if (ArrayUtils.isEqualArray(res, expected))
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}


let equations1 = [["a", "b"], ["b", "c"]];
let values1 = [2.0, 3.0];
let queries1 = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]];
let expected1 = [6.0, 0.5, -1.0, 1.0, -1.0 ];
test('test1', equations1, values1, queries1, expected1);


let equations2 = [["a","e"],["b","e"]];
let values2 = [4.0, 3.0];
let queries2 = [["a","b"],["e","e"],["x","x"]];
let expected2 = [4/3, 1.0, -1.0];
test('test2', equations2, values2, queries2, expected2);


//  Equations are given in the format A / B = k, where A and B are variables 
//  represented as strings, and k is a real number (floating point number). 
//  Given some queries, return the answers. If the answer does not exist, return -1.0.

//  Example:
//  Given a / b = 2.0, b / c = 3.0.
//  queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
//  return [6.0, 0.5, -1.0, 1.0, -1.0 ].

//  The input is: vector<pair<string, string>> equations, vector<double>& values,
//   vector<pair<string, string>> queries , where equations.size() == values.size(), 
//   and the values are positive. This represents the equations. Return vector<double>.

//  According to the example above:

//  equations = [ ["a", "b"], ["b", "c"] ],
//  values = [2.0, 3.0],
//  queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
//   

//  The input is always valid. You may assume that evaluating the queries will
//   result in no division by zero and there is no contradiction.
