import { ArrayUtils } from './utils_js/array.js';

/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function(tickets) {
  let adjs = {};

  // build graph
  for (let i = 0; i < tickets.length; i++) {
    let start = tickets[i][0], end = tickets[i][1];
    if (!adjs.hasOwnProperty(start)) adjs[start] = [];
    adjs[start].push(end);
  }

  for (const [key, value] of Object.entries(adjs)) {
    value.sort()    // 这里按照字典序排序
  }

  let res = [];
  let search = (start) => {
    while (adjs[start] && adjs[start].length) {
      search(adjs[start].shift());   // 从字典序小的开始添加。与常规dfs不同的是，这里元素添加后，要pop掉
    }
    res.push(start);                 // 必须是递归回来之后，在添加
  }
  search('JFK');

  return res.reverse();              // 因为是递归回来之后再添加的，所以要reverse
};

function test(testName, tickets, expected) {
  let res = findItinerary(tickets);
  if (ArrayUtils.isEqualArray(res, expected))
    console.log(testName + ' success.');
  else
    console.log(testName + ' failed.');
}


let tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]];
let expected1 = ["JFK", "MUC", "LHR", "SFO", "SJC"];
test('test1', tickets1, expected1);


let tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]];
let expected2 = ["JFK","ATL","JFK","SFO","ATL","SFO"];
test('test2', tickets2, expected2);


// Given a list of airline tickets represented by pairs of departure and 
// arrival airports [from, to], reconstruct the itinerary in order. 
// All of the tickets belong to a man who departs from JFK. 
// Thus, the itinerary must begin with JFK.

// Note:

// If there are multiple valid itineraries, you should return the 
// itinerary that has the smallest lexical order when read as a single string. 
// For example, the itinerary ["JFK", "LGA"] has a smaller lexical order 
// than ["JFK", "LGB"].
// All airports are represented by three capital letters (IATA code).
// You may assume all tickets form at least one valid itinerary.
// One must use all the tickets once and only once.

// Example 1:

// Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
// Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

// Example 2:

// Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
// Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]

// Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
//              But it is larger in lexical order.
